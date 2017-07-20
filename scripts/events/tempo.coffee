path = require 'path'
natural = require 'natural'
programacao = require '../programacao.json'

{msgVariables, stringElseRandomKey} = require path.join '..', 'lib', 'common.coffee'
answers = {}

currentDate = new Date
currentDate.getTimezoneOffset()

getTrilha = (programacao, trilha, now = false) ->
  currentTime = "#{currentDate.getHours()}:#{currentDate.getMinutes()}"
  programacao.filter (item) ->
    startTime = item.time[0]
    endTime = item.time[1]
    return item.track_title is trilha and ((not now and startTime > currentTime) or (now and startTime < currentTime and endTime > currentTime))

class tempo
  constructor: (@interaction) ->
  process: (msg, text, classification) =>
    type = @interaction.type?.toLowerCase() or 'random'

    variables = {
      trilha: classification[0].label
      programacao: ''
    }

    currentTalk = getTrilha programacao, variables.trilha, true
    nextTalks = getTrilha programacao, variables.trilha

    if currentTalk.length
      variables.programacao += "*Acontecendo agora*: \n" + currentTalk.map((talk) ->
        return "- *#{talk.time[0]} - #{talk.time[1]}* - #{talk.title}"
      ).join("\n")
      variables.programacao += "\n\n"

    if nextTalks.length
      variables.programacao += "*Próximas palestras*: \n" + nextTalks.map((talk) ->
        return "- *#{talk.time[0]} - #{talk.time[1]}* - #{talk.title}"
      ).join("\n")

    switch type
      when 'block'
        messages = @interaction.message.map (line) ->
          return msgVariables line, msg, variables
        msg.sendWithNaturalDelay messages
      when 'random'
        message = stringElseRandomKey @interaction.message
        message = msgVariables message, msg, variables
        msg.sendWithNaturalDelay message

module.exports = tempo
