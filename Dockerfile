FROM node:alpine

LABEL mantainer "Diego Dorgam <diego.dorgam@rocket.chat>"

ENV HUBOT_LANG='pt'                                                  \
    HUBOT_CORPUS='corpus.yml'                                        \
    HUBOT_ADAPTER=rocketchat                                         \
    HUBOT_OWNER=RocketChat                                           \
    HUBOT_NAME=HubotNatural                                          \
    HUBOT_DESCRIPTION="Processamento de linguagem natural com hubot" \
    HUBOT_LOG_LEVEL=debug                                            \
    ROCKETCHAT_URL=http://rocketchat:3000                            \
    ROCKETCHAT_ROOM=GENERAL                                          \
    ROCKETCHAT_USER=chatbot                                          \
    ROCKETCHAT_PASSWORD=@12345@                                      \
    ROCKETCHAT_AUTH=password                                         \
    RESPOND_TO_DM=true                                               \
    RESPOND_TO_LIVECHAT=true                                         \
    RESPOND_TO_EDITED=true                                           \
    LISTEN_ON_ALL_PUBLIC=false                                       \
    HUBOT_NATURAL_DEBUG_MODE=false

RUN apk --update add --no-cache git python make g++ && \
    addgroup -S hubotnat && adduser -S -g hubotnat hubotnat

USER node

RUN mkdir /home/node/.npm-global && \
    chown -R node:node /home/node/.npm-global

ENV PATH=/home/node/.npm-global/bin:$PATH \
    NPM_CONFIG_PREFIX=/home/node/.npm-global

RUN npm install -g yo generator-hubot

WORKDIR /home/hubotnat/bot

USER root

RUN mkdir -p /home/hubotnat/.config/configstore                             && \
    echo "optOut: true" > /home/hubotnat/.config/configstore/insight-yo.yml && \
    chown -R hubotnat:hubotnat /home/hubotnat

USER hubotnat

RUN yo hubot --adapter ${HUBOT_ADAPTER}         \
             --owner ${HUBOT_OWNER}             \
             --name ${HUBOT_NAME}               \
             --description ${HUBOT_DESCRIPTION} \
             --defaults --no-insight

COPY ["external-scripts.json","package.json", "/home/hubotnat/bot/"]

ADD scripts/ /home/hubotnat/bot/scripts/

ENTRYPOINT /home/hubotnat/bot/bin/hubot -a rocketchat
