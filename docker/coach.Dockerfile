FROM lappis/botrequirements:boilerplate

COPY ./bot/config.yml /coach/
COPY ./bot/domain.yml /coach/
COPY ./Makefile /coach/

RUN mkdir /src_models

WORKDIR /coach

RUN make coach-train

RUN find /. | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
