FROM requirements:latest

COPY ./coach /coach
COPY ./scripts /scripts

RUN mkdir /src_models

WORKDIR /coach

RUN make train

RUN find /. | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
