FROM node:7.7.4-wheezy
MAINTAINER Diego Dorgam <dorgam@gmail.com>

# Install CoffeeScript, Hubot
RUN \
  npm install -g coffee-script hubot yo generator-hubot natural && \
  rm -rf /var/lib/apt/lists/*

# make user for bot
# yo requires uid/gid 501
RUN groupadd -g 501 hubot1 && \
  useradd -m -u 501 -g 501 hubot1
USER hubot1
WORKDIR /home/hubot1/bot

# optionally override variables with docker run -e HUBOT_...
# Modify ./ENV file to override these options
ENV HUBOT_OWNER hubot1
ENV HUBOT_NAME hubot1
ENV HUBOT_ADAPTER rocketchat
ENV HUBOT_DESCRIPTION Just a friendly robot
ENV ROCKETCHAT_URL 'https://chat.dorgam.it'
ENV ROCKETCHAT_ROOM general
ENV RESPOND_TO_DM true
ENV ROCKETCHAT_USER chatbot
ENV ROCKETCHAT_PASSWORD @12345@
ENV ROCKETCHAT_AUTH password
ENV HUBOT_LOG_LEVEL debug

# Creating hubot
USER root
RUN mkdir -p /home/hubot1/.config/configstore && \
  echo "optOut: true" > /home/hubot1/.config/configstore/insight-yo.yml && \
  chown -R hubot1:hubot1 /home/hubot1
USER hubot1
RUN /usr/local/bin/yo hubot --adapter ${HUBOT_ADAPTER} --owner ${HUBOT_OWNER} --name ${HUBOT_NAME} --description ${HUBOT_DESCRIPTION} --defaults --no-insight
COPY ["external-scripts.json","hubot-start.sh","package.json","scripts/", "/home/hubot1/bot/"]

# make directories and files

USER root
RUN chmod +x /home/hubot1/bot/hubot-start.sh
USER hubot1

EXPOSE 80
EXPOSE 3000

#  Override adapter with --env-file ENV
ENTRYPOINT ./hubot-start.sh
