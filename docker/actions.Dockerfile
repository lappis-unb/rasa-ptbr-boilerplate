FROM rasa/rasa-sdk:3.3.0

WORKDIR /bot
COPY ./bot /bot

ENTRYPOINT []
CMD "python -m rasa_sdk -p 5055"
