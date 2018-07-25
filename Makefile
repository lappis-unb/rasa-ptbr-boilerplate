run_conversation:
	python -m rasa_core.run -d rouana/models/dialogue -u rouana/models/nlu/current -p ${ROUANA_PORT} --connector ${ROUANA_CONNECTOR} --credentials credentials.yml

run_server:
	python -m rasa_core.server -d models/dialogue -u models/nlu/default/current -o out_server.log

train:
	python -m rasa_nlu.train --config rouana/config.yml --data rouana/data/nlu_data.md --fixed_model_name current --path rouana/models/ --project nlu
	python -m rasa_core.train -s rouana/data/rouana_stories.md -d rouana/domain.yml -o rouana/models/dialogue --epochs ${ROUANA_TRAINING_EPOCHS}
