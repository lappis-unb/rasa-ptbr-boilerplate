fs = require 'fs'
path = require 'path'
natural = require 'natural'
PorterStemmerPt = require path.join '..','..','node_modules','natural','lib','natural','stemmers','porter_stemmer_pt.js'

config = {}
events = {}
nodes = {}
error_count = 0
err_nodes = 0

{regexEscape} = require path.join '..', 'lib', 'common.coffee'

eventsPath = path.join __dirname, '..', 'events'
for event in fs.readdirSync(eventsPath).sort()
  events[event.replace /\.coffee$/, ''] = require path.join eventsPath, event

classifyInteraction = (interaction, classifier, interactions) ->
  if Array.isArray interaction.classifiers
    for doc in interaction.classifiers
      classifier.addDocument(doc, interaction.node.name)
      if Array.isArray interaction.next?.interactions
        interaction.next.classifier = new natural.LogisticRegressionClassifier(PorterStemmerPt)
        for nextInteractionName in interaction.next.interactions
          nextInteraction = interactions.find (n) -> n.node.name is nextInteractionName
          classifyInteraction nextInteraction, interaction.next.classifier
        interaction.next.classifier.train()

setContext = (res, context) ->
  res.robot.brain.set('context_'+res.envelope.room, context)

getContext = (res) ->
  return res.robot.brain.get('context_'+res.envelope.room)

incErrors = (res) ->
  errors = res.robot.brain.get('errors_'+res.envelope.room) or 0
  errors++
  res.robot.brain.set('errors_'+res.envelope.room, errors)
  return errors

clearErrors = (res) ->
  res.robot.brain.set('errors_'+res.envelope.room, 0)

module.exports = (_config, robot) ->
  config = _config
  if not config.interactions?.length
    robot.logger.warning 'No interactions configured.'
    return
  if not config.trust
    robot.logger.warning 'No trust level configured.'
    return

  console.log 'Processing interactions'
  console.time 'Processing interactions (Done)'
  classifier = new natural.LogisticRegressionClassifier(PorterStemmerPt)
  #console.log(config.interactions)
  for interaction in config.interactions
    {node, classifiers, event} = interaction
    nodes[node.name] = new events[event] interaction
    # count error nodes
    if node.name.substr(0,5) == "error"
      err_nodes++
    if interaction.level != 'context'
      classifyInteraction interaction, classifier, config.interactions
  classifier.train()
  console.timeEnd 'Processing interactions (Done)'

  robot.hear /(.+)/i, (res) ->
    msg = res.match[0].replace res.robot.name+' ', ''
    msg = msg.replace(/^\s+/, '')
    msg = msg.replace(/\s+&/, '')

    context = getContext(res)
    currentClassifier = classifier

    if context
      interaction = config.interactions.find (interaction) -> interaction.node.name is context
      if interaction? and interaction.next?.classifier?
        currentClassifier = interaction.next.classifier

    classifications = currentClassifier.getClassifications(msg)

    if classifications[0].value < config.trust
      error_count = incErrors res
      if error_count > err_nodes
        clearErrors res
      node_name = "error-" + error_count
    else
      node_name = classifications[0].label

    currentNode = nodes[node_name]
    currentInteraction = config.interactions.find (interaction) -> interaction.node.name is node_name
    if currentInteraction.context == 'clear'
      setContext(res, undefined)
    else
      setContext(res, node_name)

    callback = currentNode.process
    callback.apply @, arguments
