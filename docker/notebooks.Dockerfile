from jupyter/minimal-notebook

user root

run apt-get update && apt-get install -y graphviz libgraphviz-dev pkg-config

workdir /work/


cmd jupyter-notebook --allow-root --NotebookApp.token='' --NotebookApp.password=''
