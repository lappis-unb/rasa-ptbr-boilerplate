path = require 'path'
natural = require 'natural'

{msgVariables, stringElseRandomKey} = require path.join '..', 'lib', 'common.coffee'
answers = {}

class configure
  constructor: (@interaction) ->
  process: (msg) =>
    if @interaction.roleRequired?
        #TODO: Check if user has role needed
        console.log('ROLE REQUIRED:', @interaction.roleRequired)

#    console.log msg
    configurationBlock = msg.message.text.replace(msg.robot.name + ' ', '').split(' ')[-1..].toString()
#    console.log configurationBlock
    configKeyValue = configurationBlock.split('=')
    configKey = configKeyValue[0]
    configValue = configKeyValue[1]

    console.log('Setting config ', configKeyValue)
    key = 'configure_'+configKey+'_'+msg.envelope.room
#    key = 'configure_'+configKey+'_'+msg.envelope.room+'_'+msg.envelope.user.id
    msg.robot.brain.set(key, configValue)

    type = @interaction.type?.toLowerCase() or 'random'
    switch type
      when 'block'
        messages = @interaction.answer.map (line) ->
          return msgVariables line, msg, {key:configKey, value: configValue}
        msg.sendWithNaturalDelay messages
      when 'random'
        message = stringElseRandomKey @interaction.answer
        message = msgVariables message, msg, {key:configKey, value: configValue}
        msg.sendWithNaturalDelay message

module.exports = configure
