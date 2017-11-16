fs = require 'fs'
path = require 'path'
natural = require 'natural'

lang = (process.env.HUBOT_LANG || 'en')
if lang == "en"
  PorterStemmer = require path.join '..','..','node_modules','natural','lib','natural','stemmers','porter_stemmer.js'
else
  PorterStemmer = require path.join '..','..','node_modules','natural','lib','natural','stemmers','porter_stemmer_' + lang + '.js'

debug_mode = ((process.env.HUBOT_NATURAL_DEBUG_MODE == 'true') || false)

config = {}
events = {}
nodes = {}
error_count = 0
err_nodes = 0

{regexEscape, loadConfigfile} = require path.join '..', 'lib', 'common.coffee'

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
    msg = msg.answer

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

# check these
livechatTransferHuman = (res) ->
	setTimeout ->
		res.robot.adapter.callMethod 'livechat:transfer',
			roomId: res.envelope.room
			departmentId: process.env.DEPARTMENT_ID
	, 1000

setUserName = (res, name) ->
	res.robot.adapter.callMethod 'livechat:saveInfo',
		_id: res.envelope.user.id
		name: name
	,
		_id: res.envelope.room
#

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
        nextInteraction = config.interactions.find (n) ->
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

setContext = (res, context) ->
  key = 'context_'+res.envelope.room+'_'+res.envelope.user.id
  console.log 'set context', context
  res.robot.brain.set(key, context)

getContext = (res) ->
  key = 'context_'+res.envelope.room+'_'+res.envelope.user.id
  return res.robot.brain.get(key)

isDebugMode = (res) ->
  key = 'configure_debug-mode_'+res.envelope.room+'_'+res.envelope.user.id
  return (res.robot.brain.get(key) == 'true')

getDebugCount = (res) ->
  key = 'configure_debug-count_'+res.envelope.room+'_'+res.envelope.user.id

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

module.exports = (_config, _configPath, robot) ->
  config = _config
  configPath = _configPath

  if not config.interactions?.length
    robot.logger.warning 'No interactions configured.'
    return
  if not config.trust
    robot.logger.warning 'No trust level configured.'
    return

  classifier = new natural.LogisticRegressionClassifier(PorterStemmer)

  trainBot = (retrain = false) ->
    console.log 'Processing interactions'
    console.time 'Processing interactions (Done)'

    if retrain
        nodes = {}
        classifier = new natural.LogisticRegressionClassifier(PorterStemmer)

    for interaction in config.interactions
      {name, classifiers, event} = interaction
      nodes[name] = new events[event] interaction
      # count error nodes
      if name.substr(0,5) == "error"
        err_nodes++
      if interaction.level != 'context'
        classifyInteraction interaction, classifier

    classifier.train()

    console.timeEnd 'Processing interactions (Done)'

  trainBot()

  processMessage = (res, msg) ->
    context = getContext(res)
    currentClassifier = classifier
    trust = config.trust
    interaction = undefined
    debugMode = isDebugMode(res)

    console.log 'context ->', context

    if context
      interaction = config.interactions.find (interaction) -> interaction.name is context
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
      int = config.interactions.find (interaction) ->
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
        return processMessage(res, msg)
      else
        error_count = incErrors res
        if error_count > err_nodes
          clearErrors res
        error_node_name = "error-" + error_count

    currentInteraction = config.interactions.find (interaction) ->
      interaction.name is node_name or interaction.name is error_node_name

    if not currentInteraction?
      clearErrors res
      return console.log 'Invalid interaction ['+node_name+']'

    if currentInteraction.context == 'clear'
      setContext(res, undefined)
    else if node_name?
      setContext(res, node_name)

    currentNode = nodes[node_name or error_node_name]
    currentNode.process.call @, res, msg, subClassifications

  if debug_mode
    robot.respond /bottrain/i, (res) ->
      config = loadConfigfile(configPath)
      trainBot(true)

  robot.hear /(.+)/i, (res) ->
    res.sendWithNaturalDelay = sendWithNaturalDelay.bind(res)
    msg = res.match[0].replace res.robot.name+' ', ''
    msg = msg.replace(/^\s+/, '')
    msg = msg.replace(/\s+&/, '')
    # check if robot should respond
    if res.envelope.user.roomType in ['c','p']
      if (res.message.text.match new RegExp('\\b' + res.robot.name + '\\b', 'i')) or (res.message.text.match new RegExp('\\b' + res.robot.alias + '\\b', 'i'))
        processMessage res, msg
    else if res.envelope.user.roomType in ['d','l']
      processMessage res, msg

# TODO
# make a function for checking roles
# const usersAndRoles = {};
#
# module.exports = function (robot) {
#     robot.adapter.chatdriver.callMethod('getUserRoles').then(function (users) {
#         users.forEach(function (user) {
#             user.roles.forEach(function (role) {
#                 if (typeof (usersAndRoles[role]) === 'undefined') {
#                     usersAndRoles[role] = [];
#                 }
#
#                 usersAndRoles[role].push(user.username);
#             });
#         });
#     });
#
#     robot.respond(/test/i, function (res) {
#         console.log(res);
#
#         if (usersAndRoles.admin.indexOf(res.message.user.name) === -1) {
#             res.reply('What...?');
#         } else {
#             res.reply('hello boss!');
#         }
#
#     });
# }
