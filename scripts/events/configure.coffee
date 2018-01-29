require 'coffeescript/register'

brain = require '../bot/brain'
{ msgVariables, stringElseRandomKey, loadConfigfile, getConfigFilePath } = require  '../lib/common'

class configure
  constructor: (@interaction) ->

  process: (msg) =>
    if @interaction.role?
      if checkRole(msg, @interaction.role)
        @act(msg)
      else
        msg.sendWithNaturalDelay "*Acces Denied* Action requires role #{@interaction.role}"
    else
      @act(msg)

  setVariable: (msg) ->
    configurationBlock = msg.message.text.replace(msg.robot.name + ' ', '')
      .split(' ')[-1..].toString()
    configKeyValue = configurationBlock.split('=')
    configKey = configKeyValue[0]
    configValue = configKeyValue[1]
    key = 'configure_' + configKey + '_' + msg.envelope.room
    msg.robot.brain.set(key, configValue)
    type = @interaction.type?.toLowerCase() or 'random'
    switch type
      when 'block'
        messages = @interaction.answer.map (line) ->
          return msgVariables line, msg, { key: configKey, value: configValue }
        msg.sendWithNaturalDelay messages
      when 'random'
        message = stringElseRandomKey @interaction.answer
        message = msgVariables message, msg, { key: configKey, value: configValue }
        msg.sendWithNaturalDelay message
    return

  retrain: (msg) ->
    global.config = loadConfigfile getConfigFilePath()
    brain.train()

    type = @interaction.type?.toLowerCase() or 'random'
    switch type
      when 'block'
        messages = @interaction.answer.map (line) ->
          return msgVariables line, msg
        msg.sendWithNaturalDelay messages
      when 'random'
        message = stringElseRandomKey @interaction.answer
        message = msgVariables message, msg
        msg.sendWithNaturalDelay message
    return

  act: (msg) ->
    action = @interaction.action or 'setVariable'
    console.log action
    switch action
      when 'setVariable'
        @setVariable(msg)
      when 'train'
        @retrain(msg)
    return

module.exports = configure
