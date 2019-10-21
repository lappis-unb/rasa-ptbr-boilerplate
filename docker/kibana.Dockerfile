FROM docker.elastic.co/kibana/kibana:7.3.0

COPY modules/analytics/import_dashboards.py analytics/import_dashboards.py
COPY modules/analytics/dashboards.json analytics/dashboards.json

USER root

RUN yum -y update
RUN yum -y install yum-utils
RUN yum -y groupinstall development
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm
RUN yum -y install python36u
RUN yum -y install python36u-pip

RUN pip3.6 install requests

USER kibana

WORKDIR /usr/share/kibana/analytics
