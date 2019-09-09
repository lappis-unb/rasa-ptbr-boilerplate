FROM docker.elastic.co/elasticsearch/elasticsearch:7.3.0

RUN mkdir backup

RUN chown -R elasticsearch:elasticsearch backup
