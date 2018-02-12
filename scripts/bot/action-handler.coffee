actionHandler = {}

fs = require 'fs'
path = require 'path'

actionsPath = path.join __dirname, '..', 'actions'
actions = {}

nodes = {}
err_nodes = 0

actionHandler.registerActions = (config) ->
  for action in fs.readdirSync(actionsPath).sort()
    action_name = action.replace /\.coffee$/, ''
    actions[action_name] = require path.join actionsPath, action

  for interaction in config.interactions
    { name, action } = interaction
    nodes[name] = new actions[action] interaction

    if name.substr(0, 5) == "error"
      err_nodes++

actionHandler.errorNodesCount = () ->
  return err_nodes

actionHandler.takeAction = (name, res) ->
  nodes[name].process(res)

module.exports = actionHandler
