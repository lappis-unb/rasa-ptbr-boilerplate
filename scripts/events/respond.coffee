path = require 'path'
natural = require 'natural'

{msgVariables, stringElseRandomKey} = require path.join '..', 'lib', 'common.coffee'
answers = {}

class respond
  constructor: (@interaction) ->
  process: (msg) =>
    type = @interaction.type?.toLowerCase() or 'random'
    switch type
      when 'block'
        messages = @interaction.message.map (line) ->
          return msgVariables line, msg
        msg.sendWithNaturalDelay messages
      when 'random'
        message = stringElseRandomKey @interaction.message
        message = msgVariables message, msg
        msg.sendWithNaturalDelay message

module.exports = respond
