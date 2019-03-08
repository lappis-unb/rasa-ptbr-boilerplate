train-nlu:
	python3 -m rasa_nlu.train -c nlu_config.yml --fixed_model_name current --data data/intents/ -o models --project nlu --verbose

train-core:
	python3 train.py

train: train-nlu train-core

run-rocketchat:
	python3 run-rocketchat.py

run-console:
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/current --debug --endpoints endpoints.yml

run-api:
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/current --endpoints endpoints.yml --debug --enable_api 

train-online:
	python3 -m rasa_core.train -d domain.yml -s data/stories -o models/dialogue --epochs 15 --online --nlu models/nlu/current/

evaluate:
	python3 -m rasa_core.evaluate -d models/dialogue -s data/core/

run-actions:
	python -m rasa_core_sdk.endpoint --actions actions
