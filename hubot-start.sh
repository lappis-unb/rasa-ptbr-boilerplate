#!/bin/bash

# script used to detect if hubot has already been generated

if [[ -x /home/hubot1/bot/bin/hubot ]]; then
  bin/hubot -a rocketchat
else
  /usr/local/bin/yo hubot --adapter ${HUBOT_ADAPTER} --owner ${HUBOT_OWNER} --name ${HUBOT_NAME} --description ${HUBOT_DESCRIPTION} --defaults --no-insight
fi
