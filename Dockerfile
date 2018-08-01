from python:3.6

env TRAINING_EPOCHS=300

run apt-get install -y git
run pip install rasa_core rasa_nlu[spacy] && \
    python -m spacy download pt

run mkdir /rouana
add . /rouana

cmd python -m rasa_nlu.train                   \
           --config /rouana/config.yml         \
           --data   /rouana/data/nlu_data.md   \
           --fixed_model_name current          \
           --path /models                      \
           --project nlu                    && \
    python -m rasa_core.train                  \
           -s /rouana/data/rouana_stories.md   \
           -d /rouana/domain.yml               \
           -o /models/dialogue                 \
           --epochs ${TRAINING_EPOCHS}      && \
    python -m rasa_core.run                    \
           -d /models/dialogue                 \
           -u /models/nlu/current              \
           --debug
