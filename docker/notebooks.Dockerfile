FROM python:3.6-slim

RUN apt update && apt install -y git gcc make curl

RUN python -m pip install --upgrade pip

ADD ./bot.requirements.txt /tmp

RUN pip install -r /tmp/bot.requirements.txt
RUN python -c "import nltk; nltk.download('stopwords');"

RUN apt-get update && apt-get install -y graphviz libgraphviz-dev pkg-config

# Pygraphviz depends on package graphviz wich needs to be configurated
# acording to each OS. because of it it's not added to bot.requirements
RUN pip install jupyter pygraphviz==1.5

WORKDIR /work/

CMD jupyter-notebook --allow-root --NotebookApp.token='' --ip=0.0.0.0 --NotebookApp.password=''
