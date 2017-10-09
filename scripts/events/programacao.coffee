path = require 'path'
natural = require 'natural'

{msgVariables, stringElseRandomKey} = require path.join '..', 'lib', 'common.coffee'
answers = {}

class programacao
  constructor: (@interaction) ->
  process: (msg) =>
    # localizar a trilha na mensagem do usuário

    # carregar o json com a programacao
    programa = require './programacao.json'

    #encontra a trilha e retorna a programação deste horário

    type = @interaction.type?.toLowerCase() or 'random'
    switch type
      when 'block'
        @interaction.message.forEach (line) ->
          message = msgVariables line, msg
          msg['send'] message
      when 'random'
        message = stringElseRandomKey @interaction.message
        message = msgVariables message, msg
        msg['send'] message

module.exports = programacao
