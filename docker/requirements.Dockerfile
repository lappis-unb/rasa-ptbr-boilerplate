FROM python:3.7.9-slim


ARG BOT_DIR=./bot

COPY $BOT_DIR/requirements.txt /tmp
COPY $BOT_DIR/x-requirements.txt /tmp
COPY $BOT_DIR/Makefile /tmp

RUN apt-get update                                                             && \
    apt-get install -y gcc make build-essential

RUN useradd -m rasa
USER rasa
WORKDIR /bot
ENV PATH="/home/rasa/.local/bin:${PATH}"

RUN pip install --upgrade pip                                                  && \
    make  -C /tmp install                                                      && \
    make  -C /tmp install-x                                                    && \
    python -c "import nltk; nltk.download(['stopwords', 'rslp', 'punkt']);"    && \
    find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
