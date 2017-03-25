#!/bin/bash

# script used to detect if hubot has already been generated

if [[ -x /home/hubot/bot/bin/hubot ]]; then
  bin/hubot
else
  /usr/local/bin/yo hubot --adapter ${HUBOT_ADAPTER} --owner ${HUBOT_OWNER} --name ${HUBOT_NAME} --description ${HUBOT_DESCRIPTION} --defaults --no-insight
fi
