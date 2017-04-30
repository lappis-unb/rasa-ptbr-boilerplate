fs = require 'fs'
yaml = require 'js-yaml'
path = require 'path'
chatbot = require path.join __dirname, 'bot', 'index.coffee'

hubotPath = module.parent.filename
hubotPath = path.dirname hubotPath for [1..4]
configPath = path.join hubotPath, 'scripts', 'config', 'corpus.yml'

try
  config = yaml.safeLoad fs.readFileSync configPath, 'utf8'
catch err
  console.error "An error occurred while trying to load bot's config."
  console.error err
  process.exit()

chatbot = chatbot.bind null, config

module.exports = chatbot
