fs = require 'fs'
path = require 'path'
natural = require 'natural'

config = {}
events = {}
answers = {}

{regexEscape} = require path.join '..', 'lib', 'common.coffee'

eventsPath = path.join __dirname, '..', 'events'
for event in fs.readdirSync(eventsPath).sort()
  events[event.replace /\.coffee$/, ''] = require path.join eventsPath, event

module.exports = (_config, robot) ->
  config = _config
  if not config.interactions?.length
    robot.logger.warning 'No interactions configured.'
    return

  classifier = new natural.BayesClassifier()
  config.interactions.forEach (interaction) ->
    {node, classifiers, message, event} = interaction
    if not events.hasOwnProperty event
      console.log "Unknown event #{event}"
      return
    event = new events[event] interaction
    event._first_run = true
    callback = event.process

    #regex = message.replace '$botname', regexEscape robot.name
    #regex = message.regex.replace '$user', regexEscape user.name
    answers[node.name] = message
    trigger = interaction.trigger or 'hear'

    classifiers.forEach (doc) ->
      classifier.addDocument(doc, node.name)

  classifier.train()

  robot.hear /(.+)/i, (res) ->
    msg = res.match[0].replace res.robot.name+' ', ''
    msg = msg.replace(/^\s+/, '')
    msg = msg.replace(/\s+&/, '')
    nameInteraction = classifier.classify(msg)
    resposta = answers[nameInteraction]
    res.send "#{resposta}"
#fix this

    # robot[trigger] new RegExp(regex, pattern.options or 'i'), do (event, interaction, callback) ->
    #   ->
    #     if event._first_run or Math.random() < (interaction.probability or config.probability)
    #       callback.apply @, arguments
    #       event._first_run = false
