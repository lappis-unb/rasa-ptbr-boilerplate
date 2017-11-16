path = require 'path'

{loadConfigfile} = require path.join path.join __dirname, 'lib', 'common.coffee'
chatbot = require path.join __dirname, 'bot', 'index.coffee'

hubotPath = module.parent.filename
hubotPath = path.dirname hubotPath for [1..4]
corpus = (process.env.HUBOT_CORPUS || 'corpus.yml')
configPath = path.join hubotPath, 'training_data', corpus

try
  config = loadConfigfile configPath
catch err
  process.exit()

chatbot = chatbot.bind null, config, configPath

module.exports = chatbot
