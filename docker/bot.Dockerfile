FROM lappis/coach:boilerplate as coach
FROM lappis/botrequirements:boilerplate

WORKDIR /bot

COPY ./bot /bot
COPY ./modules /modules
COPY --from=coach /src_models/ /bot/models/

RUN chown -R 1001 /bot/models && chmod -R 750 /bot/models

RUN find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
