FROM requirements:latest

COPY ./bot /bot
COPY ./scripts /scripts

WORKDIR /bot

ENV ROCKETCHAT_URL=rocketchat:3000         \
    MAX_TYPING_TIME=10                     \
    MIN_TYPING_TIME=1                      \
    WORDS_PER_SECOND_TYPING=5              \
    ROCKETCHAT_ADMIN_USERNAME=admin        \
    ROCKETCHAT_ADMIN_PASSWORD=admin        \
    ROCKETCHAT_BOT_USERNAME=tais           \
    ROCKETCHAT_BOT_PASSWORD=tais           \
    ENVIRONMENT_NAME=localhost             \
    BOT_VERSION=last-commit-hash           \
    ENABLE_ANALYTICS=False                 \
    ELASTICSEARCH_URL=elasticsearch:9200   

RUN find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

CMD python /scripts/bot_config.py -r $ROCKETCHAT_URL                        \
    -an $ROCKETCHAT_ADMIN_USERNAME -ap $ROCKETCHAT_ADMIN_PASSWORD    \
    -bu $ROCKETCHAT_BOT_USERNAME -bp $ROCKETCHAT_BOT_PASSWORD \
    && make run-rocketchat
