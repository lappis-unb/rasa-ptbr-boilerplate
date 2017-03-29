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
        @interaction.message.forEach (line) ->
          msg['send'] line
      when 'random'
        message = stringElseRandomKey @interaction.message
        message = msgVariables message, msg
        msg['send'] message

module.exports = respond
