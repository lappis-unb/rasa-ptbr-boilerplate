from python:3.6

env TRAINING_EPOCHS=300

run apt-get install -y git
run pip install rasa_core rasa_nlu[spacy] && \
    python -m spacy download pt

run mkdir /rouana
add ./roauna /rouana

workdir /rouana

cmd python train.py all
