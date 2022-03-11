FROM rasa/rasa:3.0.8

WORKDIR /bot
COPY ./bot /bot
COPY ./modules /modules

USER root
RUN apt install make
USER 1001

RUN export PYTHONPATH=/bot/components/:$PYTHONPATH

ENTRYPOINT []
CMD []
