require 'coffeescript/register'

{ msgVariables, sendMessages, stringElseRandomKey } = require '../lib/common'

class Error
  constructor: (@interaction) ->
  process: (msg) =>
    sendMessages(stringElseRandomKey(@interaction.answer), msg)

module.exports = Error
