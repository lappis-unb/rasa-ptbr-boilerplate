FROM botrequirements as coach

WORKDIR /bot

COPY ./bot/ /bot/

RUN make train
