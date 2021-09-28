FROM arthurtemporim/boilerplate:latest

RUN useradd -m rasa
USER rasa

WORKDIR /bot
COPY ./bot /bot
COPY ./modules /modules

RUN export PYTHONPATH=/bot/components/:$PYTHONPATH
