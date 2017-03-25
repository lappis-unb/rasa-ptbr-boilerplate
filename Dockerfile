FROM node:4.4.3-slim
MAINTAINER Diego Dorgam <dorgam@gmail.com>

# Install CoffeeScript, Hubot
RUN \
  npm install -g coffee-script hubot yo generator-hubot natural && \
  rm -rf /var/lib/apt/lists/*

# make user for bot
# yo requires uid/gid 501
RUN groupadd -g 501 hubot && \
  useradd -m -u 501 -g 501 hubot

COPY ["external-scripts.json","hubot-start.sh","package.json","scripts/", "/home/hubot/bot/"]

# make directories and files
RUN mkdir -p /home/hubot/.config/configstore && \
  echo "optOut: true" > /home/hubot/.config/configstore/insight-yo.yml && \
  chown -R hubot:hubot /home/hubot && \
  chmod +x /home/hubot/bot/hubot-start.sh

USER hubot
WORKDIR /home/hubot/bot

# optionally override variables with docker run -e HUBOT_...
# Modify ./ENV file to override these options
ENV HUBOT_OWNER hubot
ENV HUBOT_NAME hubot
ENV HUBOT_ADAPTER rocketchat
ENV HUBOT_DESCRIPTION Just a friendly robot

# Override adapter with --env-file ENV
ENTRYPOINT ./hubot-start.sh
