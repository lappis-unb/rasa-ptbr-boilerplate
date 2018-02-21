require 'coffeescript/register'

{ msgVariables, sendMessages, stringElseRandomKey } = require '../lib/common'

livechat_department = (process.env.LIVECHAT_DEPARTMENT_ID || null )

class Respond
  constructor: (@interaction) ->
  process: (msg) =>
    lc_dept = @interaction.department or livechat_department
    offline_message = (
      @interaction.offline or 'Sorry, there is no online agents to transfer to.'
    )
    sendMessages(stringElseRandomKey(@interaction.answer), msg)

    command = @interaction.command?.toLowerCase() or false
    switch command
      when 'transfer'
        @livechatTransfer(msg, 3000, lc_dept, offline_message)


  livechatTransfer: (msg, delay = 3000, lc_dept, offline_message) ->
    setTimeout((-> msg.robot.adapter.callMethod('livechat:transfer',
                      roomId: msg.envelope.room
                      departmentId: lc_dept
                    ).then (result) ->
                      if result == true
                        console.log 'livechatTransfer executed!'
                      else
                        console.log 'livechatTransfer NOT executed!'
                        sendMessages(stringElseRandomKey(offline_message), msg)
                ), delay)

module.exports = Respond
