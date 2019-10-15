FROM lappis/botrequirements:boilerplate

COPY ./bot/ /coach/

RUN mkdir /src_models

WORKDIR /coach

RUN make train

RUN find /. | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
