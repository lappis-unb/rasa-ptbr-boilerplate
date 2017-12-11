#!/bin/bash
export HUBOT_ADAPTER=rocketchat
export HUBOT_OWNER=RocketChat
export HUBOT_NAME='CatBot'
export HUBOT_DESCRIPTION="Processamento de linguagem natural com hubot"
export ROCKETCHAT_URL=https://chat.dorgam.it
export ROCKETCHAT_ROOM=GENERAL
export RESPOND_TO_DM=true
export RESPOND_TO_LIVECHAT=true
export ROCKETCHAT_USER=catbot
export ROCKETCHAT_PASSWORD='GatoNoTelhado'
export ROCKETCHAT_AUTH=password
export HUBOT_LOG_LEVEL=debug
export HUBOT_CORPUS='catbot-en.yml'
export HUBOT_LANG='en'
bin/hubot -a rocketchat
