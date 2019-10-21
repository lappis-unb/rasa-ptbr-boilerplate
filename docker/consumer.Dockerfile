FROM python:3.6-slim

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir -I pika==1.1.0 elasticsearch==6.3.1 nltk==3.3 certifi==2019.3.9
RUN python -c "import nltk; nltk.download('stopwords');"
RUN find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
