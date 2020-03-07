FROM python:3.6-slim

COPY ./requirements.txt /tmp

RUN apt update && apt install -y gcc make && \
    python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt && \
    python -c "import nltk; nltk.download('stopwords');"

RUN find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
