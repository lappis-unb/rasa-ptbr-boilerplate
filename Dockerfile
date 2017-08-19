FROM node:alpine

LABEL mantainer "Diego Dorgam <diego.dorgam@rocket.chat>"

ENV LISTEN_ON_ALL_PUBLIC=false RESPOND_TO_DM=true RESPOND_TO_EDITED=true HUBOT_CORPUS='corpus.yml' HUBOT_ADAPTER=rocketchat HUBOT_OWNER=RocketChat HUBOT_NAME=HubotNatural HUBOT_DESCRIPTION="Processamento de linguagem natural com hubot" ROCKETCHAT_URL=http://rocketchat:3000 ROCKETCHAT_ROOM=GENERAL RESPOND_TO_DM=true ROCKETCHAT_USER=chatbot ROCKETCHAT_PASSWORD=@12345@ ROCKETCHAT_AUTH=password HUBOT_LOG_LEVEL=debug

RUN \
  npm install -g coffee-script hubot yo generator-hubot natural js-yaml

RUN addgroup -S hubotnat && adduser -S -g hubotnat hubotnat

WORKDIR /home/hubotnat/bot

RUN mkdir -p /home/hubotnat/.config/configstore && \
  echo "optOut: true" > /home/hubotnat/.config/configstore/insight-yo.yml && \
  chown -R hubotnat:hubotnat /home/hubotnat

RUN apk update && apk add git

USER hubotnat

RUN /usr/local/bin/yo hubot --adapter ${HUBOT_ADAPTER} --owner ${HUBOT_OWNER} --name ${HUBOT_NAME} --description ${HUBOT_DESCRIPTION} --defaults --no-insight

COPY ["external-scripts.json","package.json", "/home/hubotnat/bot/"]

ADD scripts/ /home/hubotnat/bot/scripts/

# EXPOSE 80 3000

USER hubotnat

ENTRYPOINT /home/hubotnat/bot/bin/hubot -a rocketchat
