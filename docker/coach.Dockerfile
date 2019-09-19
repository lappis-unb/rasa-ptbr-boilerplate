FROM lappis/botrequirements:boilerplate

COPY ./coach /coach
COPY ./modules/ /modules

RUN mkdir /src_models

WORKDIR /coach

RUN make train

RUN find /. | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
