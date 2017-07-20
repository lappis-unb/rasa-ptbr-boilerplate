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

typing = (res, t) ->
  res.robot.adapter.callMethod 'stream-notify-room', res.envelope.user.roomID+'/typing', res.robot.alias, t is true

sendWithNaturalDelay = (msgs, elapsed=0) ->
  if !Array.isArray msgs
    msgs = [msgs]

  keysPerSecond = 50
  maxResponseTimeInSeconds = 2

  msg = msgs.shift()
  if typeof msg isnt 'string'
    cb = msg.callback
    msg = msg.message

  delay = Math.min(Math.max((msg.length / keysPerSecond) * 1000 - elapsed, 0), maxResponseTimeInSeconds * 1000)
  typing @, true
  setTimeout =>
    @send msg

    if msgs.length
      sendWithNaturalDelay.call @, msgs
    else
      typing @, false
      cb?()
  , delay


classifyInteraction = (interaction, classifier) ->
  if Array.isArray interaction.classifiers
    for doc in interaction.classifiers
      if interaction.multi == true
        classifier.addDocument(doc, interaction.node.name+'|'+doc)
      else
        classifier.addDocument(doc, interaction.node.name)

    if Array.isArray interaction.next?.interactions
      interaction.next.classifier = new natural.LogisticRegressionClassifier(PorterStemmerPt)
      for nextInteractionName in interaction.next.interactions
        nextInteraction = config.interactions.find (n) ->
          return n.node.name is nextInteractionName
        if not nextInteraction?
          console.log 'No valid interaction for', nextInteractionName
          continue
        classifyInteraction nextInteraction, interaction.next.classifier
      interaction.next.classifier.train()

    if interaction.multi == true
      interaction.classifier = new natural.LogisticRegressionClassifier(PorterStemmerPt)
      for doc in interaction.classifiers
        interaction.classifier.addDocument(doc, doc)
      interaction.classifier.train()

setContext = (res, context) ->
  key = 'context_'+res.envelope.room+'_'+res.envelope.user.id
  console.log 'set context', context
  res.robot.brain.set(key, context)

getContext = (res) ->
  key = 'context_'+res.envelope.room+'_'+res.envelope.user.id
  return res.robot.brain.get(key)

incErrors = (res) ->
  key = 'errors_'+res.envelope.room+'_'+res.envelope.user.id
  errors = res.robot.brain.get(key) or 0
  errors++
  console.log 'inc errors', errors
  res.robot.brain.set(key, errors)
  return errors

clearErrors = (res) ->
  console.log 'clear errors'
  key = 'errors_'+res.envelope.room+'_'+res.envelope.user.id
  res.robot.brain.set(key, 0)

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
      classifyInteraction interaction, classifier
  classifier.train()
  console.timeEnd 'Processing interactions (Done)'

  processMessage = (res, msg) ->
    context = getContext(res)
    currentClassifier = classifier
    trust = config.trust
    interaction = undefined

    console.log 'context ->', context

    if context
      interaction = config.interactions.find (interaction) -> interaction.node.name is context
      if interaction? and interaction.next?.classifier?
        currentClassifier = interaction.next.classifier

        if interaction.next.trust?
          trust = interaction.next.trust

    classifications = currentClassifier.getClassifications(msg)

    console.log 'classifications ->', classifications

    if classifications[0].value >= trust
      clearErrors res
      [node_name, sub_node_name] = classifications[0].label.split('|')
      console.log({node_name, sub_node_name})
      int = config.interactions.find (interaction) ->
        interaction.node.name is node_name
      if int.classifier?
        subClassifications = int.classifier.getClassifications(msg)
    else
      if Array.isArray interaction?.next?.error
        error_count = incErrors res
        error_node_name = interaction.next.error[error_count - 1]
        if not error_node_name?
          clearErrors res
          error_node_name = interaction.next.error[0]
      else if interaction?.next?
        setContext(res, undefined)
        return processMessage(res, msg)
      else
        error_count = incErrors res
        if error_count > err_nodes
          clearErrors res
        error_node_name = "error-" + error_count

    currentInteraction = config.interactions.find (interaction) ->
      interaction.node.name is node_name or interaction.node.name is error_node_name

    if not currentInteraction?
      clearErrors res
      return console.log 'Invalid interaction ['+node_name+']'

    if currentInteraction.context == 'clear'
      setContext(res, undefined)
    else if node_name?
      setContext(res, node_name)

    currentNode = nodes[node_name or error_node_name]
    currentNode.process.call @, res, msg, subClassifications


  robot.hear /(.+)/i, (res) ->
    res.sendWithNaturalDelay = sendWithNaturalDelay.bind(res)
    msg = res.match[0].replace res.robot.name+' ', ''
    msg = msg.replace(/^\s+/, '')
    msg = msg.replace(/\s+&/, '')

    processMessage res, msg
