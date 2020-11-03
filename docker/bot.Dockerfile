FROM botrequirements

WORKDIR /bot
COPY ./bot /bot
COPY ./modules /modules

ENV GIT_PYTHON_REFRESH quiet

RUN find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
