#!/bin/bash
export HUBOT_ADAPTER=rocketchat
export HUBOT_OWNER=RocketChat
export HUBOT_NAME='CatBot'
export HUBOT_DESCRIPTION="Processamento de linguagem natural com hubot"
#export ROCKETCHAT_URL=https://demo.rocket.chat
export ROCKETCHAT_URL=https://chat.dorgam.it
#export ROCKETCHAT_ROOM=j8pjQdHtZR5JnGF2S
export ROCKETCHAT_ROOM=GENERAL
export RESPOND_TO_DM=true
export RESPOND_TO_LIVECHAT=true
export ROCKETCHAT_USER=catbot
export ROCKETCHAT_PASSWORD='@cat!bot'
export ROCKETCHAT_AUTH=password
export HUBOT_LOG_LEVEL=debug
export HUBOT_CORPUS='rocket-small.yml'
bin/hubot -a rocketchat --name $HUBOT_NAME
