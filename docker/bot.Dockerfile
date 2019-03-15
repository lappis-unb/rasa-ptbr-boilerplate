from python:3.6-slim

run apt update && apt install -y git gcc make curl

run python -m pip install --upgrade pip

add ./bot.requirements.txt /tmp

run pip install --upgrade pip && pip install -r /tmp/bot.requirements.txt
run python -c "import nltk; nltk.download('stopwords');"

add ./bot /bot
add ./scripts /scripts

workdir /bot

env TRAINING_EPOCHS=20                    \
    ROCKETCHAT_URL=rocketchat:3000         \
    MAX_TYPING_TIME=10                     \
    MIN_TYPING_TIME=1                      \
    WORDS_PER_SECOND_TYPING=5              \
    ROCKETCHAT_ADMIN_USERNAME=admin        \
    ROCKETCHAT_ADMIN_PASSWORD=admin        \
    ROCKETCHAT_BOT_USERNAME=bot            \
    ROCKETCHAT_BOT_PASSWORD=bot            \
    ENVIRONMENT_NAME=localhost             \
    BOT_VERSION=last-commit-hash           \
    ENABLE_ANALYTICS=False                 \
    ELASTICSEARCH_URL=elasticsearch:9200

cmd python /scripts/bot_config.py -r $ROCKETCHAT_URL                        \
           -an $ROCKETCHAT_ADMIN_USERNAME -ap $ROCKETCHAT_ADMIN_PASSWORD    \
           -bu $ROCKETCHAT_BOT_USERNAME -bp $ROCKETCHAT_BOT_PASSWORD     && \
    make train && make run-rocketchat
