require 'coffeescript/register'

{ loadConfigfile, getConfigFilePath } = require  './lib/common'
chatbot = require './bot/index'

try
  global.config = loadConfigfile getConfigFilePath()
catch err
  process.exit()

chatbot = chatbot.bind null, global.config

module.exports = chatbot
