from python:3.6

run apt-get install -y git


run git clone https://github.com/lappis-unb/rasa_core.git  && \
    cd rasa_core                                           && \
    pip install -r requirements.txt                        && \
    pip install -e .

run pip install rasa-nlu[spacy]==0.13.0   && \
    python -m spacy download pt

run mkdir /rouana

add ./rouana /rouana
workdir /rouana

env TRAINING_EPOCHS=300                    \
    CREDENTIALS="/rouana/credentials.yml"  \
    ROUANA_PORT=5005

cmd python train-rocketchat.py
