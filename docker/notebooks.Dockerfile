FROM botrequirements

RUN apt-get update && apt-get install -y graphviz libgraphviz-dev pkg-config

# Pygraphviz depends on package graphviz wich needs to be configurated
# acording to each OS. because of it it's not added to bot.requirements
RUN pip install jupyter pygraphviz==1.5

COPY ./bot /bot

WORKDIR /work/

CMD jupyter-notebook --allow-root --NotebookApp.token='' --ip=0.0.0.0 --NotebookApp.password=''
