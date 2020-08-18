FROM docker.elastic.co/kibana/kibana:7.8.1

COPY modules/analytics/import_dashboards.py analytics/import_dashboards.py
COPY modules/analytics/dashboards.json analytics/dashboards.json

USER root

RUN yum -y update
RUN yum -y install yum-utils
RUN yum -y groupinstall development
RUN yum install -y https://repo.ius.io/ius-release-el7.rpm
RUN yum -y install python36u
RUN yum -y install python36u-pip

RUN pip3.6 install requests

USER kibana

WORKDIR /usr/share/kibana/analytics
