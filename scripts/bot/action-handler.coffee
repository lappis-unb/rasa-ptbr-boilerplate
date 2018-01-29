actionHandler = {}

fs = require 'fs'
path = require 'path'

eventsPath = path.join __dirname, '..', 'events'
events = {}

nodes = {}
err_nodes = 0

actionHandler.registerActions = (config) ->
  for event in fs.readdirSync(eventsPath).sort()
    events[event.replace /\.coffee$/, ''] = require path.join eventsPath, event

  for interaction in config.interactions
    { name, event } = interaction
    nodes[name] = new events[event] interaction

    if name.substr(0, 5) == "error"
      err_nodes++

actionHandler.errorNodesCount = () ->
  return err_nodes

actionHandler.takeAction = (name, res) ->
  nodes[name].process(res)

module.exports = actionHandler
