fs = require 'fs'
path = require 'path'
natural = require 'natural'
PorterStemmerPt = require path.join '..','..','node_modules','natural','lib','natural','stemmers','porter_stemmer_pt.js'

config = {}
events = {}
nodes = {}
error_count = 0
err_nodes = 0

{regexEscape} = require path.join '..', 'lib', 'common.coffee'

eventsPath = path.join __dirname, '..', 'events'
for event in fs.readdirSync(eventsPath).sort()
  events[event.replace /\.coffee$/, ''] = require path.join eventsPath, event

module.exports = (_config, robot) ->
  config = _config
  if not config.interactions?.length
    robot.logger.warning 'No interactions configured.'
    return
  if not config.trust
    robot.logger.warning 'No trust level configured.'
    return

  classifier = new natural.LogisticRegressionClassifier(PorterStemmerPt)
  #console.log(config.interactions)
  config.interactions.forEach (interaction) ->
    {node, classifiers, event} = interaction
    nodes[node.name] = new events[event] interaction
    # count error nodes
    if node.name.substr(0,5) == "error"
      err_nodes++

    if classifiers instanceof Array
      classifiers.forEach (doc) ->
        classifier.addDocument(doc, node.name)
  classifier.train()

  robot.hear /(.+)/i, (res) ->
    msg = res.match[0].replace res.robot.name+' ', ''
    msg = msg.replace(/^\s+/, '')
    msg = msg.replace(/\s+&/, '')
    if classifier.getClassifications(msg)[0].value < config.trust
      error_count++
      if error_count > err_nodes then error_count=1
      node_name = "error-" + error_count
    else
      node_name = classifier.classify(msg)

    callback = nodes[node_name].process
    callback.apply @, arguments
