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

env TRAINING_EPOCHS=300                    \
    CREDENTIALS="/rouana/credentials.yml"  \
    ROCKETCHAT_URL="http://rocketchat:3000"

cmd python /scripts/bot_config.py -r $ROCKETCHAT_URL && python train-rocketchat.py
