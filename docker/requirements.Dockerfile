FROM python:3.8.9-slim-buster 

ARG BOT_DIR=./bot

COPY $BOT_DIR/requirements.txt /tmp
COPY $BOT_DIR/x-requirements.txt /tmp
COPY $BOT_DIR/Makefile /tmp

RUN apt-get update                                                             && \
    apt-get install -y gcc make build-essential git                            && \
    make  -C /tmp install                                                      && \
    rasa telemetry disable                                                     && \
    python -c "import nltk; nltk.download(['stopwords', 'rslp', 'punkt']);"    && \
    find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf               && \
    apt-get clean                                                              && \
    apt-get remove -y build-essential
