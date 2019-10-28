FROM botrequirements

WORKDIR /bot

COPY ./bot/ /bot/

RUN make train
