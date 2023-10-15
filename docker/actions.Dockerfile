FROM rasa/rasa-sdk:3.6.2

WORKDIR /bot
COPY ./bot /bot

ENTRYPOINT []
CMD "python -m rasa_sdk -p 5055"
