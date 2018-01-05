path = require 'path'
natural = require 'natural'

{msgVariables, stringElseRandomKey} = require path.join '..', 'lib', 'common.coffee'
answers = {}
livechat_department = (process.env.LIVECHAT_DEPARTMENT_ID || null )

class respond
  constructor: (@interaction) ->
  process: (msg) =>
    action = @interaction.action?.toLowerCase() or false
    switch action
      when 'transfer'
        @livechatTransfer(msg)

    type = @interaction.type?.toLowerCase() or 'random'
    switch type
      when 'block'
        messages = @interaction.answer.map (line) ->
          return msgVariables line, msg
        msg.sendWithNaturalDelay messages, 0, action
      when 'random'
        message = stringElseRandomKey @interaction.answer
        message = msgVariables message, msg
        msg.sendWithNaturalDelay message, 0, action

  livechatTransfer: (msg) ->
    setTimeout ( -> msg.robot.adapter.callMethod('livechat:transfer',
                      roomId: msg.envelope.room
                      departmentId: livechat_department
                      ).then (result) ->
                        console.log 'livechatTransfer executed! ' + result
    ), 3000


module.exports = respond
