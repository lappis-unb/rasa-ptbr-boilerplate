path = require 'path'
natural = require 'natural'

{ msgVariables, stringElseRandomKey } = require path.join '..', 'lib', 'common.coffee'
answers = {}
livechat_department = (process.env.LIVECHAT_DEPARTMENT_ID || null )

class respond
  constructor: (@interaction) ->
  process: (msg) =>
    lc_dept = @interaction.department or livechat_department
    offline_message = @interaction.offline or 'Sorry, there is no online agents to transfer to.'
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

    action = @interaction.action?.toLowerCase() or false
    switch action
      when 'transfer'
        @livechatTransfer(msg, 3000, lc_dept, offline_message, type)


  livechatTransfer: (msg, delay = 3000, lc_dept, offline_message, type) ->
    setTimeout((-> msg.robot.adapter.callMethod('livechat:transfer',
                      roomId: msg.envelope.room
                      departmentId: lc_dept
                    ).then (result) ->
                      if result == true
                        console.log 'livechatTransfer executed!'
                      else
                        console.log 'livechatTransfer NOT executed!'
                        switch type
                          when 'block'
                            messages = offline_message.map (line) ->
                              return msgVariables line, msg
                            msg.sendWithNaturalDelay messages
                          when 'random'
                            message = stringElseRandomKey offline_message
                            message = msgVariables message, msg
                            msg.sendWithNaturalDelay message
                ), delay)

module.exports = respond
