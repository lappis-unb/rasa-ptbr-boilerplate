FROM jupyter/minimal-notebook

ADD ./intent-requirements.txt /tmp/

USER root

RUN apt-get update         \
    && apt-get upgrade -yq \
    && apt-get install -yq graphviz libgraphviz-dev pkg-config

USER jovyan

RUN pip install -r /tmp/intent-requirements.txt

RUN python -m spacy download pt

ADD ./bot-intent-lab.ipynb /home/jovyan/work/
