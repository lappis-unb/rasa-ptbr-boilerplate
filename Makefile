run_conversation:
	python -m rasa_core.run -d rouana/models/dialogue -u rouana/models/nlu/current -p 5005 --connector rocketchat --credentials rouana/credentials.yml

run_server:
	python -m rasa_core.server -d models/dialogue -u models/nlu/default/current -o out_server.log

train:
	python -m rasa_nlu.train --config rouana/config_spacy.yml --data rouana/data/salic_preenchimento.md --fixed_model_name current --path rouana/models/ --project nlu
	#python bot.py train-dialogue
	python -m rasa_core.train -s rouana/data/rouana_stories.md -d rouana/domain.yml -o rouana/models/dialogue --epochs 300
