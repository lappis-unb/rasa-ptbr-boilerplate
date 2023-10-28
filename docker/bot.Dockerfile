ARG RASA_VERSION
FROM rasa/rasa:${RASA_VERSION}-full

WORKDIR /bot
COPY ./bot /bot
COPY ./modules /modules

USER root
RUN apt-get install make && \
    make install

ENTRYPOINT []
CMD []
