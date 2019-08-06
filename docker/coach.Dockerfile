FROM lappis/botrequirements:boilerplate

COPY ./coach /coach
COPY ./scripts /scripts

RUN mv /coach/nginx.conf /etc/nginx/conf.d/nginx.conf

RUN mkdir /src_models
WORKDIR /coach
RUN make train


WORKDIR /
RUN tar -czvf models.tar.gz /src_models/
RUN md5sum models.tar.gz > model_version.txt

RUN mkdir notebook_models
RUN cp -r /src_models/* /notebook_models

RUN find /. | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

CMD ["nginx", "-g", "daemon off;"]