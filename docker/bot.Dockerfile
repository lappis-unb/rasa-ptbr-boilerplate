FROM botrequirements

WORKDIR /bot

COPY ./bot /bot
COPY ./modules /modules

RUN find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
