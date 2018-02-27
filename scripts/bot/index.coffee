require 'coffeescript/register'

{ regexEscape, loadConfigfile } = require '../lib/common'
{ getUserRoles, checkRole } = require '../lib/security'
actionHandler = require './action-handler'
classifier = require './classifier'

typing = (res, t) ->
  res.robot.adapter.callMethod 'stream-notify-room',
    res.envelope.user.roomID + '/typing', res.robot.alias, t is true

sendWithNaturalDelay = (msgs, elapsed = 0) ->
  if !Array.isArray msgs
    msgs = [msgs]

  keysPerSecond = 50
  maxResponseTimeInSeconds = 2

  msg = msgs.shift()
  if typeof msg isnt 'string'
    cb = msg.callback
    msg = msg.answer

  minTimeTyping = maxResponseTimeInSeconds * 1000
  timeToType = (msg.length / keysPerSecond) * 1000 - elapsed
  delay = Math.min(Math.max(timeToType, 0), minTimeTyping)
  typing @, true

  setTimeout =>
    @send msg

    if msgs.length
      sendWithNaturalDelay.call @, msgs
    else
      typing @, false
      cb?()
  , delay

createMatch = (text, pattern) ->
  return text.match new RegExp('\\b' + pattern + '\\b', 'i')

module.exports = (_config, robot) ->
  global.config = _config

  global.usersAndRoles = getUserRoles(robot)

  if not global.config.interactions?.length
    robot.logger.warning 'No interactions configured.'
    return
  if not global.config.trust
    robot.logger.warning 'No trust level configured.'
    return

  actionHandler.registerActions(global.config)
  classifier.train()

  robot.hear /(.+)/i, (res) ->
    res.sendWithNaturalDelay = sendWithNaturalDelay.bind(res)
    msg = (res.match[0].replace res.robot.name + ' ', '').trim()

    # check if robot should respond
    if res.envelope.user.roomType in ['c', 'p']
      if (createMatch(res.message.text, res.robot.name) or
          createMatch(res.message.text, res.robot.alias))
        actionName = classifier.processMessage(res, msg)
        actionHandler.takeAction(actionName, res)
        # TODO: Add engaged user conversation recognition/tracking
    else if res.envelope.user.roomType in ['d', 'l']
      actionName = classifier.processMessage(res, msg)
      actionHandler.takeAction(actionName, res)
