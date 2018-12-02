from python:3.6-slim

user root

run apt update && apt install -y git gcc make curl

run python -m pip install --upgrade pip

add ./bot.requirements.txt /tmp

run pip install --no-cache-dir -r /tmp/bot.requirements.txt

run apt-get update && apt-get install -y graphviz libgraphviz-dev pkg-config

run pip install jupyter

workdir /work/

cmd jupyter-notebook --allow-root --NotebookApp.token='' --ip=0.0.0.0 --NotebookApp.password=''
