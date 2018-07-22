from registry.gitlab.com/lappis-unb/services/rouana/rasa_core

add . /opt/rouana

run python -m spacy download pt

workdir /opt/rouana

cmd bash -c "make train && make run_conversation"
