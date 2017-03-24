common = {}

common.applyVariable = (string, variable, value, regexFlags = 'i') ->
  string.replace new RegExp("(^|\\W)\\$#{variable}(\\W|$)", regexFlags), (match) ->
    match.replace "$#{variable}", value

common.msgVariables = (message, msg) ->
  message = common.applyVariable message, 'user', msg.envelope.user.name
  message = common.applyVariable message, 'heartbot', msg.robot.name
  message = common.applyVariable message, 'room', msg.envelope.room if msg.envelope.room?

common.stringElseRandomKey = (variable) ->
  return variable if typeof variable is 'string'

  if variable instanceof Array
    variable[Math.floor(Math.random() * variable.length)]

common.regexEscape = (string) ->
  #http://stackoverflow.com/a/6969486
  string.replace /[\-\[\]\/\{\}\(\)\*\+\?\.\\\^\$\|]/g, "\\$&"

module.exports = common