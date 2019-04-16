train-nlu:
	python3 -m rasa_nlu.train -c nlu_config.yml --fixed_model_name current \
  --data data/intents/ -o models --project nlu --verbose

train-core:
	python3 train.py

train: train-nlu train-core

run-rocketchat:
	python3 run-rocketchat.py

run-telegram:
	python -m rasa_core.run -d models/dialogue -u models/nlu/current --port 5001 --credentials credentials.yml --endpoints endpoints.yml

run-console:
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/current \
  --debug --endpoints endpoints.yml

run-api:
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/current \
  --endpoints endpoints.yml --debug --enable_api 

train-online:
	python -m rasa_core.train        \
  interactive -o models/dialogue     \
  -d domain.yml -c policy_config.yml \
  -s data/stories                    \
  --nlu models/nlu/current/          \
  --endpoints endpoints.yml


evaluate:
	python3 -m rasa_core.evaluate -d models/dialogue -s data/core/

run-actions:
	python -m rasa_core_sdk.endpoint --actions actions
