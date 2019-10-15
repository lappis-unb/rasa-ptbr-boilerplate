FROM lappis/coach:boilerplate as coach
FROM lappis/botrequirements:boilerplate

WORKDIR /bot

COPY ./bot /bot
COPY ./Makefile /bot/Makefile
COPY ./modules /modules
COPY --from=coach /src_models/ /bot/models/

RUN find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
