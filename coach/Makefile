train-nlu:
	rasa train nlu -vv                 \
	--config nlu_config.yml            \
	--fixed-model-name current         \
	--nlu data/intents/                \
	--out /src_models

train-core:
	rasa train core -vv                \
	--config core_config.yml           \
	-d domain.yml                      \
	-s data/stories/                   \
	--out /src_models/dialogue/

train: train-nlu train-core
