FROM rasa/rasa:3.4.2-full

WORKDIR /bot
COPY ./bot /bot
COPY ./modules /modules

USER root
RUN apt-get install make && \
    make install

ENTRYPOINT []
CMD []
