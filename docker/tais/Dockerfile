from python:3.6

run apt-get install -y git

add ./requirements.txt /tmp

run pip install -r /tmp/requirements.txt  && \
    python -m spacy download pt

run pip uninstall -y tensorflow && pip install tensorflow==1.5

run apt-get remove --purge -y git         && \
    mkdir /rouana

add ./rouana /rouana
workdir /rouana

add ./scripts /scripts

env TRAINING_EPOCHS=300                     \
    CREDENTIALS=credentials.yml             \
    ROCKETCHAT_URL=rocketchat:3000          \
    MAX_TYPING_TIME=10                      \
    MIN_TYPING_TIME=1                       \
    WORDS_PER_SECOND_TYPING=5               \
    ROCKETCHAT_ADMIN_USERNAME=admin                    \
    ROCKETCHAT_ADMIN_PASSWORD=admin                    \
    ROCKETCHAT_TAIS_USERNAME=tais                      \
    ROCKETCHAT_TAIS_PASSWORD=tais                      \
    TRAINED_DATA_FOLDER=/

cmd python /scripts/bot_config.py -r $ROCKETCHAT_URL    \
           -an $ROCKETCHAT_ADMIN_USERNAME -ap $ROCKETCHAT_ADMIN_PASSWORD      \
           -bu $ROCKETCHAT_TAIS_USERNAME -bp $ROCKETCHAT_TAIS_PASSWORD     && \
    python train-rocketchat.py
