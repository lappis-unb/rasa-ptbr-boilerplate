path = require 'path'
{msgVariables, stringElseRandomKey} = require path.join '..', 'lib', 'common.coffee'

class respond
  constructor: (@interaction) ->
  process: (msg) =>
    messageType = @interaction.type?.toLowerCase() or 'respond'
    switch messageType
      when 'exec', 'emote'
        messageType = 'emote'
      else
        messageType = 'send'

    message = stringElseRandomKey @interaction.message

    message = msgVariables message, msg
    msg[messageType] message

module.exports = respond
