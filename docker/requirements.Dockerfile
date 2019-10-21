FROM python:3.6-slim as botrequirements

RUN apt update && apt install -y gcc make

RUN python -m pip install --upgrade pip

COPY ./requirements.txt /tmp

RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN python -c "import nltk; nltk.download('stopwords');"
RUN find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
