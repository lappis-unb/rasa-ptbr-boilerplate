FROM lappis/botrequirements:boilerplate

COPY ./coach /coach
COPY ./scripts /scripts

RUN mv /coach/base_config/nginx.conf /etc/nginx/conf.d/nginx.conf
RUN mv /coach/base_config/* /

RUN mkdir /src_models

RUN make train

RUN ./compress_models.sh

RUN mkdir notebook_models
RUN cp -r /src_models/* /notebook_models

RUN find /. | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

CMD ["nginx", "-g", "daemon off;"]