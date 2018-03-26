fs = require 'fs'
yaml = require 'js-yaml'

common = {}

applyVariable = (string, variable, value, regexFlags = 'i') ->
  console.log(string)
  string.replace(
    new RegExp("(^|\\W)\\$#{variable}(\\W|$)", regexFlags),
    (match) ->
      match.replace "$#{variable}", value
  )

common.msgVariables = (message, msg, variables = {}) ->
  message = applyVariable message, 'user', msg.envelope.user.name
  message = applyVariable message, 'bot', msg.robot.alias
  if (msg.envelope.room?)
    message = applyVariable message, 'room', msg.envelope.room

  for key, value of variables
    message = common.applyVariable message, key, value
  return message

common.stringElseRandomKey = (variable) ->
  return variable if typeof variable is 'string'
  if variable instanceof Array
    variable[Math.floor(Math.random() * variable.length)]

common.sendMessages = (messages, msg, variables = {}) ->
  console.log(messages)
  if !Array.isArray messages
    messages = [messages]
  messages = messages.map (message) ->
    return common.msgVariables message, msg, variables
  msg.sendWithNaturalDelay messages

getYAMLFiles = (filepath) ->
  listFile = fs.readdirSync filepath
  dataFiles = []
  if listFile.length > 0
    dataFiles = listFile.map (filename) ->
      return yaml.safeLoad fs.readFileSync filepath + '/' + filename, 'utf8'
  else
    console.error('The directory: ' + filepath + ' is empty.')
  return dataFiles

concatYAMLFiles = (dataFiles) ->
  mindBot = {}
  if dataFiles.length > 0
    mindBot = { trust: dataFiles[0].trust, interactions: [] }
    dataFiles.forEach (element) ->
      mindBot.trust = Math.min(mindBot.trust, element.trust)
      mindBot.interactions = mindBot.interactions.concat element.interactions
  else
    console.error('Data files is empty.')
  return mindBot

common.regexEscape = (string) ->
  #http://stackoverflow.com/a/6969486
  string.replace /[\-\[\]\/\{\}\(\)\*\+\?\.\\\^\$\|]/g, "\\$&"

common.getConfigFilePath = () ->
  return process.env.HUBOT_CORPUS || 'training_data/corpus.yml'

common.loadConfigfile = (filepath) ->
  try
    console.log("Loading corpus: " + filepath)

    if fs.lstatSync(filepath).isFile()
      return yaml.safeLoad fs.readFileSync filepath, 'utf8'

    else if fs.lstatSync(filepath).isDirectory()
      yamlFiles = getYAMLFiles(filepath)
      return concatYAMLFiles(yamlFiles)

  catch err
    console.error "An error occurred while trying to load bot's config."
    console.error err
    throw Error("Error on loading YAML file " + filepath)

module.exports = common
