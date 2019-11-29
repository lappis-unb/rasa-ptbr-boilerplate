FROM lappis/coach:boilerplate as coach
FROM botrequirements

WORKDIR /bot
COPY ./bot /bot
COPY --from=coach /bot/models /bot/models
COPY ./modules /modules

RUN find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
