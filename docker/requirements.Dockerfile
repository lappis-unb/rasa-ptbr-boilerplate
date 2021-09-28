FROM python:3.7.12-slim-bullseye

ARG BOT_DIR=./bot

COPY $BOT_DIR/requirements.txt /tmp
COPY $BOT_DIR/x-requirements.txt /tmp
COPY $BOT_DIR/Makefile /tmp

RUN apt-get update                                                             && \
    apt-get install -y gcc make build-essential git                            && \
    pip install --upgrade pip                                                  && \
    make  -C /tmp install-x                                                    && \
    rasa telemetry disable                                                     && \
    #python -c "import nltk; nltk.download(['stopwords', 'rslp', 'punkt']);"    && \
    find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf               && \
    apt-get clean                                                              && \
    apt-get remove -y build-essential
