FROM docker.elastic.co/elasticsearch/elasticsearch:6.4.2

RUN mkdir backup

RUN chown -R elasticsearch:elasticsearch backup