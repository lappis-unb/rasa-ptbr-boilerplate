from python:3.6

run apt-get install -y git

add ./requirements.txt /tmp

run pip install -r /tmp/requirements.txt  && \
    python -m spacy download pt

run apt-get remove --purge -y git         && \
    mkdir /rouana

add ./rouana /rouana
workdir /rouana

env TRAINING_EPOCHS=300                    \
    CREDENTIALS="/rouana/credentials.yml"

cmd python train-rocketchat.py
