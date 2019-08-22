ARG BOT_CONTAINER
FROM ${BOT_CONTAINER}

COPY ./bot /bot
COPY ./scripts /scripts

WORKDIR /bot


RUN find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf