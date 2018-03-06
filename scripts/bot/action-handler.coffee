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

  if err_nodes == 0
    console.log("WARNING! You don't have any error nodes, you need at least " +
                "one to garantee that the bot always will respond something")

actionHandler.errorNodesCount = () ->
  return err_nodes

actionHandler.takeAction = (name, res) ->
  if not name?
    res.sendWithNaturalDelay "I'm sorry Dave, I'm afraid I can't do that =/"
  else
    nodes[name].process(res)

module.exports = actionHandler
