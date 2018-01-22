require 'coffeescript/register'

path = require 'path'
fs = require 'fs'

{loadConfigfile, getConfigFilePath} = require  './lib/common'
chatbot = require './bot/index'

try
  global.config = loadConfigfile getConfigFilePath()
catch err
  process.exit()

chatbot = chatbot.bind null, global.config

module.exports = chatbot
