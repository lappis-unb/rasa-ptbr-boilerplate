FROM node:7.7.4-wheezy
MAINTAINER Diego Dorgam <dorgam@gmail.com>

# Install CoffeeScript, Hubot
RUN \
  npm install -g coffee-script hubot yo generator-hubot natural && \
  rm -rf /var/lib/apt/lists/*

# make user for bot
# yo requires uid/gid 501

RUN groupadd -g 501 hubotnatural && \
  useradd -m -u 501 -g 501 hubotnatural

WORKDIR /home/hubotnatural/bot

# Creating hubot
RUN mkdir -p /home/hubotnatural/.config/configstore && \
  echo "optOut: true" > /home/hubotnatural/.config/configstore/insight-yo.yml && \
  chown -R hubotnatural:hubotnatural /home/hubotnatural

USER hubotnatural

ENV HUBOT_OWNER hubotnatural
ENV HUBOT_NAME hubotnatural
ENV HUBOT_ADAPTER rocketchat
ENV HUBOT_DESCRIPTION Processamento de linguagem natural com hubot
ENV ROCKETCHAT_URL 'https://rocketchat:3000'
ENV ROCKETCHAT_ROOM general
ENV RESPOND_TO_DM true
ENV ROCKETCHAT_USER chatbot
ENV ROCKETCHAT_PASSWORD @12345@
ENV ROCKETCHAT_AUTH password
ENV HUBOT_LOG_LEVEL debug

RUN /usr/local/bin/yo hubot --adapter ${HUBOT_ADAPTER} --owner ${HUBOT_OWNER} --name ${HUBOT_NAME} --description ${HUBOT_DESCRIPTION} --defaults --no-insight
COPY ["external-scripts.json","hubot-start.sh","package.json", "/home/hubotnatural/bot/"]
ADD scripts/ /home/hubotnatural/bot/scripts/

# make directories and files
USER root
RUN chmod +x /home/hubotnatural/bot/hubot-start.sh

EXPOSE 80
EXPOSE 3000

#  Override adapter with --env-file ENV
USER hubotnatural
ENTRYPOINT /home/hubotnatural/bot/bin/hubot -a rocketchat
