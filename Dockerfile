FROM node:7.7.4-wheezy

LABEL mantainer "Diego Dorgam <diego.dorgam@rocket.chat>"

RUN \
  npm install -g coffee-script hubot yo generator-hubot natural && \
  rm -rf /var/lib/apt/lists/*

RUN groupadd -g 501 hubotnatural && \
  useradd -m -u 501 -g 501 hubotnatural

WORKDIR /home/hubotnatural/bot

RUN mkdir -p /home/hubotnatural/.config/configstore && \
  echo "optOut: true" > /home/hubotnatural/.config/configstore/insight-yo.yml && \
  chown -R hubotnatural:hubotnatural /home/hubotnatural

USER hubotnatural

ENV HUBOT_ADAPTER=rocketchat HUBOT_OWNER=RocketChat HUBOT_NAME=HubotNatural HUBOT_DESCRIPTION="Processamento de linguagem natural com hubot" ROCKETCHAT_URL=http://rocketchat:3000 ROCKETCHAT_ROOM=general RESPOND_TO_DM=true ROCKETCHAT_USER=chatbot ROCKETCHAT_PASSWORD=@12345@ ROCKETCHAT_AUTH=password HUBOT_LOG_LEVEL=debug

RUN /usr/local/bin/yo hubot --adapter ${HUBOT_ADAPTER} --owner ${HUBOT_OWNER} --name ${HUBOT_NAME} --description ${HUBOT_DESCRIPTION} --defaults --no-insight

COPY ["external-scripts.json","package.json", "/home/hubotnatural/bot/"]

ADD scripts/ /home/hubotnatural/bot/scripts/

EXPOSE 80 3000

USER hubotnatural
ENTRYPOINT /home/hubotnatural/bot/bin/hubot -a rocketchat
