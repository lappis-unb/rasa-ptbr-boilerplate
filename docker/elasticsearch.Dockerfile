FROM docker.elastic.co/elasticsearch/elasticsearch:7.8.1

RUN mkdir backup

RUN chown -R elasticsearch:elasticsearch backup
