FROM jupyter/minimal-notebook

USER root

RUN apt-get update         \
    && apt-get upgrade -yq

RUN apt-get install -yq graphviz libgraphviz-dev pkg-config

ADD ./evaluation/intent-requirements.txt /tmp/

RUN pip install -r /tmp/intent-requirements.txt

WORKDIR /work/

RUN python -m spacy download pt
