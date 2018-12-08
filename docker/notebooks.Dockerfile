from python:3.6-slim

user root

run apt update && apt install -y git gcc make curl

run python -m pip install --upgrade pip

add ./bot.requirements.txt /tmp

run pip install --no-cache-dir -r /tmp/bot.requirements.txt

run apt-get update && apt-get install -y graphviz libgraphviz-dev pkg-config

# Pygraphviz depends on package graphviz wich needs to be configurated
# acording to each SO. because of it it's not added to bot.requirements
run pip install jupyter pygraphviz==1.5

workdir /work/

cmd jupyter-notebook --allow-root --NotebookApp.token='' --ip=0.0.0.0 --NotebookApp.password=''
