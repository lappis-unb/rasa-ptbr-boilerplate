train-nlu:
	python3 -m rasa_nlu.train -c /coach/config/nlu_config.yml --fixed_model_name current \
	--data /coach/data/intents/ -o /src_models --project nlu --verbose

train-core:
	python3 /train.py

train: train-nlu train-core

# train-online:
# 	python -m rasa_core.train        \
#   interactive -o models/dialogue     \
#   -d domain.yml -c /coach/config/policy_config.yml \
#   -s data/stories                    \
#   --nlu /src_models/nlu/current/          \
#   --endpoints /coach/config/endpoints.yml
