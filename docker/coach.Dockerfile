FROM lappis/botrequirements:boilerplate

COPY ./bot/ /coach/
COPY ./bot/ /coach/
COPY ./Makefile /coach/

RUN mkdir /src_models

WORKDIR /coach

RUN make coach-train

RUN find /. | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
