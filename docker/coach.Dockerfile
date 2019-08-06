FROM lappis/botrequirements:boilerplate

COPY ./coach /coach
COPY ./scripts /scripts

RUN mv /coach/nginx.conf /etc/nginx/conf.d/nginx.conf

RUN mkdir /src_models
WORKDIR /coach
RUN make train


WORKDIR /

RUN make train

RUN find /. | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

CMD ["nginx", "-g", "daemon off;"]