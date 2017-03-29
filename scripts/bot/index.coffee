fs = require 'fs'
path = require 'path'
natural = require 'natural'

config = {}
events = {}
nodes = {}

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
    {node, classifiers, event} = interaction
    nodes[node.name] = new events[event] interaction
    classifiers.forEach (doc) ->
      classifier.addDocument(doc, node.name)

  classifier.train()
  robot.hear /(.+)/i, (res) ->
    msg = res.match[0].replace res.robot.name+' ', ''
    msg = msg.replace(/^\s+/, '')
    msg = msg.replace(/\s+&/, '')
    callback = nodes[classifier.classify(msg)].process
    callback.apply @, arguments
