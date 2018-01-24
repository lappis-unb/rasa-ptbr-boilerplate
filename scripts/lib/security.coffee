security = {}

security.getUserRoles = (robot) ->
  usersAndRoles = {}
  robot.adapter.chatdriver.callMethod('getUserRoles').then (users) ->
    users.forEach (user) ->
      user.roles.forEach (role) ->
        if typeof usersAndRoles[role] == 'undefined'
          usersAndRoles[role] = []
        usersAndRoles[role].push user.username
        return
      return
    return
  return usersAndRoles


security.checkRole = (msg, role) ->
  if typeof global.usersAndRoles[role] != 'undefined'
    if global.usersAndRoles[role].indexOf(msg.envelope.user.name) == -1
      return false
    else
      return true
  else
    msg.robot.logger.info 'Role ' + role + ' not found'
    return false

module.exports = security
