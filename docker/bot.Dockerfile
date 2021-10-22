FROM arthurtemporim/boilerplate:latest

WORKDIR /bot
COPY ./bot /bot
COPY ./modules /modules

RUN export PYTHONPATH=/bot/components/:$PYTHONPATH
