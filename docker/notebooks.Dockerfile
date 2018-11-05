from jupyter/minimal-notebook

user root

run apt-get update && apt-get install -y graphviz libgraphviz-dev pkg-config

add ./notebooks/requirements.txt /tmp/
run pip install  --no-cache-dir -r /tmp/requirements.txt

workdir /work/

run python -m spacy download pt

cmd jupyter-notebook --allow-root --NotebookApp.token='' --NotebookApp.password=''
