require 'coffeescript/register'

natural = require 'natural'

classifier = {}

lang = (process.env.HUBOT_LANG || 'en')

PorterStemmer = natural.PorterStemmer
if lang != 'en'
  lang_captilize = lang.charAt(0).toUpperCase() + lang.slice(1)
  PorterStemmer = natural['PorterStemmer' + lang_captilize]

actionHandler = require './action-handler'

# Classifier that holds all root level interactions
root_classifier = {}
error_count = 0

ROOT_LEVEL_NAME = "root"

classifyInteraction = (interaction, classifier) ->
  if not interaction.expect?
    console.warn("\t!! Interaction with no expects: " + interaction.name)
    return

  console.log('\tProcessing interaction: ' + interaction.name)

  if not Array.isArray interaction.expect
    interaction.expect = [interaction.expect]

  for doc in interaction.expect
    classifier.addDocument(doc, interaction.name)

  if interaction.next?.interactions?
    if not Array.isArray interaction.next.interactions
      interactions.next.interactions = [interactions.next.interactions]

    interaction.next.classifier = new natural.LogisticRegressionClassifier(
      PorterStemmer
    )
    for nextInteractionName in interaction.next.interactions
      nextInteraction = global.config.interactions.find (n) ->
        return n.name is nextInteractionName
      if not nextInteraction?
        console.log 'No valid interaction for', nextInteractionName
        continue
      classifyInteraction nextInteraction, interaction.next.classifier
    interaction.next.classifier.train()

classifier.train = () ->
  console.log 'Processing interactions'
  console.time 'Processing interactions (Done)'

  root_classifier = new natural.LogisticRegressionClassifier(PorterStemmer)

  for interaction in global.config.interactions
    if (not interaction.level? or
        (Array.isArray(interaction.level) and interaction.level.includes(ROOT_LEVEL_NAME)) or
        interaction.level == ROOT_LEVEL_NAME)
      classifyInteraction interaction, root_classifier

  console.log 'Training Bot (This could be take a while...)'
  root_classifier.train()

  console.timeEnd 'Processing interactions (Done)'

setContext = (res, context) ->
  key = 'context_' + res.envelope.room + '_' + res.envelope.user.id
  console.log 'set context', context
  res.robot.brain.set(key, context)

getContext = (res) ->
  key = 'context_' + res.envelope.room + '_' + res.envelope.user.id
  return res.robot.brain.get(key)

isDebugMode = (res) ->
  key = 'configure_debug-mode_' + res.envelope.room
  return (res.robot.brain.get(key) == 'true')

getDebugCount = (res) ->
  key = 'configure_debug-count_' + res.envelope.room
  if res.robot.brain.get(key)
    return res.robot.brain.get(key) - 1
  else
    return false

buildClassificationDebugMsg = (res, classifications) ->
  list = ''
  debugCount = getDebugCount(res)

  if debugCount
    classifications = classifications[0..debugCount]

  for classification, i in classifications
    list = (list.concat 'Label: ' + classification.label + ' Score: ' +
              classification.value + '\n')

  newMsg = {
    channel: res.envelope.user.roomID,
    msg: "Classifications considered:",
    attachments: [{
        text: list
    }]
  }

  return newMsg

incErrors = (res) ->
  key = 'errors_' + res.envelope.room + '_' + res.envelope.user.id
  errors = res.robot.brain.get(key) or 0
  errors++
  console.log 'inc errors ', errors
  res.robot.brain.set(key, errors)
  return errors

clearErrors = (res) ->
  console.log 'clear errors'
  key = 'errors_' + res.envelope.room + '_' + res.envelope.user.id
  res.robot.brain.set(key, 0)

classifier.processMessage = (res, msg) ->
  context = getContext(res)
  currentClassifier = root_classifier
  trust = global.config.trust
  interaction = undefined
  debugMode = isDebugMode(res)
  console.log 'context ->', context

  if context
    interaction = global.config.interactions.find (interaction) ->
      interaction.name is context
    if interaction? and interaction.next?.classifier?
      currentClassifier = interaction.next.classifier
      if interaction.next.trust?
        trust = interaction.next.trust

  classifications = currentClassifier.getClassifications(msg)

  console.log 'classifications ->', classifications[0..4]

  if debugMode
    newMsg = buildClassificationDebugMsg(res, classifications)
    robot.adapter.chatdriver.customMessage(newMsg)

  if classifications[0].value >= trust
    clearErrors res
    [node_name, sub_node_name] = classifications[0].label.split('|')
    console.log({ node_name, sub_node_name })
    int = global.config.interactions.find (interaction) ->
      interaction.name is node_name
    if int.classifier?
      int.classifier.getClassifications(msg)
  else
    if Array.isArray interaction?.next?.error
      error_count = incErrors res
      error_node_name = interaction.next.error[error_count - 1]
      if not error_node_name?
        clearErrors res
        error_node_name = interaction.next.error[0]
    else if interaction?.next?
      setContext(res, undefined)
      return classifier.processMessage(res, msg)
    else
      error_count = incErrors res

      if error_count > actionHandler.errorNodesCount()
        clearErrors res
        error_count = incErrors res

      error_node_name = "error-" + error_count

  currentInteraction = global.config.interactions.find (interaction) ->
    interaction.name is node_name or interaction.name is error_node_name

  if not currentInteraction?
    clearErrors res
    return console.log 'Invalid interaction [' + node_name + ']'

  if currentInteraction.context == 'clear'
    setContext(res, undefined)
  else if node_name?
    setContext(res, node_name)

  return node_name or error_node_name

module.exports = classifier
