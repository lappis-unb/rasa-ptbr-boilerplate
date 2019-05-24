train-nlu:
	python3 -m rasa_nlu.train -c nlu_config.yml --fixed_model_name current \
	--data data/intents/ -o /src_models --project nlu --verbose

train-core:
	python3 train.py

train: train-nlu train-core

train-online:
	python -m rasa_core.train        \
  interactive -o models/dialogue     \
  -d domain.yml -c policy_config.yml \
  -s data/stories                    \
  --nlu models/nlu/current/          \
  --endpoints endpoints.yml

run-validator:
	python3 validator.py --intents data/intents/ --stories data/stories --domain domain.yml
