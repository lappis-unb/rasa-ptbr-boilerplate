run-rocketchat:
	python3 run-rocketchat.py

run-telegram:
	python -m rasa_core.run -d /models/dialogue -u /models/nlu/current --port 5001 --credentials credentials.yml --endpoints endpoints.yml

config-rocket:
	python /scripts/bot_config.py

run-console:
	python3 -m rasa_core.run -d /models/dialogue -u /models/nlu/current \
  --debug --endpoints endpoints.yml

run-api:
	python3 -m rasa_core.run -d /models/dialogue -u /models/nlu/current \
  --endpoints endpoints.yml --debug --enable_api 

evaluate:
	python3 -m rasa_core.evaluate -d /models/dialogue -s data/core/

run-actions:
	python -m rasa_core_sdk.endpoint --actions actions


