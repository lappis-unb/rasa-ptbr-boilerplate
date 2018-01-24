natural = require 'natural'

brain = {}

lang = (process.env.HUBOT_LANG || 'en')

PorterStemmer = natural.PorterStemmer
if lang != 'en'
  PorterStemmer = require '../../node_modules/natural/lib/natural/stemmers/porter_stemmer_' + lang + '.js'

nodes = {}
error_count = 0
err_nodes = 0

classifyInteraction = (interaction, classifier) ->
  if Array.isArray interaction.expect
    for doc in interaction.expect
      if interaction.multi == true
        classifier.addDocument(doc, interaction.name+'|'+doc)
      else
        classifier.addDocument(doc, interaction.name)

    if Array.isArray interaction.next?.interactions
      interaction.next.classifier = new natural.LogisticRegressionClassifier(PorterStemmer)
      for nextInteractionName in interaction.next.interactions
        nextInteraction = global.config.interactions.find (n) ->
          return n.name is nextInteractionName
        if not nextInteraction?
          console.log 'No valid interaction for', nextInteractionName
          continue
        classifyInteraction nextInteraction, interaction.next.classifier
      interaction.next.classifier.train()

    if interaction.multi == true
      interaction.classifier = new natural.LogisticRegressionClassifier(PorterStemmer)
      for doc in interaction.expect
        interaction.classifier.addDocument(doc, doc)
      interaction.classifier.train()

brain.train = () ->
  console.log 'Processing interactions'
  console.time 'Processing interactions (Done)'

  global.nodes = {}
  global.classifier = new natural.LogisticRegressionClassifier(PorterStemmer)

  for interaction in global.config.interactions
    {name, event} = interaction
    global.nodes[name] = new global.events[event] interaction
    # count error nodes
    if name.substr(0,5) == "error"
      err_nodes++
    if interaction.level != 'context'
      classifyInteraction interaction, global.classifier

  global.classifier.train()

  console.timeEnd 'Processing interactions (Done)'

setContext = (res, context) ->
  key = 'context_'+res.envelope.room+'_'+res.envelope.user.id
  console.log 'set context', context
  res.robot.brain.set(key, context)

getContext = (res) ->
  key = 'context_'+res.envelope.room+'_'+res.envelope.user.id
  return res.robot.brain.get(key)

isDebugMode = (res) ->
  key = 'configure_debug-mode_'+res.envelope.room
  return (res.robot.brain.get(key) == 'true')

getDebugCount = (res) ->
  key = 'configure_debug-count_'+res.envelope.room
  return if res.robot.brain.get(key) then res.robot.brain.get(key) - 1 else false

buildClassificationDebugMsg = (res, classifications) ->
  list = ''
  debugCount = getDebugCount(res)

  if debugCount
    classifications = classifications[0..debugCount]

  for classification, i in classifications
    list = list.concat 'Label: ' + classification.label + ' Score: ' + classification.value + '\n'

  newMsg = {
    channel: res.envelope.user.roomID,
    msg: "Classifications considered:",
    attachments: [{
        text: list
    }]
  }

  return newMsg

incErrors = (res) ->
  key = 'errors_'+res.envelope.room+'_'+res.envelope.user.id
  errors = res.robot.brain.get(key) or 0
  errors++
  console.log 'inc errors ', errors
  res.robot.brain.set(key, errors)
  return errors

clearErrors = (res) ->
  console.log 'clear errors'
  key = 'errors_'+res.envelope.room+'_'+res.envelope.user.id
  res.robot.brain.set(key, 0)

brain.processMessage = (res, msg) ->
  context = getContext(res)
  currentClassifier = global.classifier
  trust = global.config.trust
  interaction = undefined
  debugMode = isDebugMode(res)
  console.log 'context ->', context

  if context
    interaction = global.config.interactions.find (interaction) -> interaction.name is context
    if interaction? and interaction.next?.classifier?
      currentClassifier = interaction.next.classifier

      if interaction.next.trust?
        trust = interaction.next.trust

  classifications = currentClassifier.getClassifications(msg)

  console.log 'classifications ->', classifications[0..4]

  if debugMode
    newMsg = buildClassificationDebugMsg(res, classifications)
    robot.adapter.chatdriver.customMessage(newMsg);

  if classifications[0].value >= trust
    clearErrors res
    [node_name, sub_node_name] = classifications[0].label.split('|')
    console.log({node_name, sub_node_name})
    int = global.config.interactions.find (interaction) ->
      interaction.name is node_name
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
      return brain.processMessage(res, msg)
    else
      error_count = incErrors res
      if error_count > err_nodes
        clearErrors res
      error_node_name = "error-" + error_count

  currentInteraction = global.config.interactions.find (interaction) ->
    interaction.name is node_name or interaction.name is error_node_name

  if not currentInteraction?
    clearErrors res
    return console.log 'Invalid interaction ['+node_name+']'

  if currentInteraction.context == 'clear'
    setContext(res, undefined)
  else if node_name?
    setContext(res, node_name)

  currentNode = global.nodes[node_name or error_node_name]
  currentNode.process.call @, res, msg, subClassifications

module.exports = brain
