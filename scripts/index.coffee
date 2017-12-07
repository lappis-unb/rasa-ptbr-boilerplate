path = require 'path'

{loadConfigfile} = require path.join path.join __dirname, 'lib', 'common.coffee'
chatbot = require path.join __dirname, 'bot', 'index.coffee'

hubotPath = module.parent.filename
hubotPath = path.dirname hubotPath for [1..4]
corpus = (process.env.HUBOT_CORPUS || 'corpus.yml')
global.configPath = path.join hubotPath, 'training_data', corpus

try
  global.config = loadConfigfile global.configPath
catch err
  process.exit()

chatbot = chatbot.bind null, global.config, global.configPath

module.exports = chatbot
