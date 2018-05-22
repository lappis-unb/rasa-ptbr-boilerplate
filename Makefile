run_conversation:
	python -m rasa_core.run -d models/dialogue -u rouana/models/nlu/default/model_20180507-125040/ -p 5005 --connector rocketchat --credentials rasa_core/credentials.yml 

run_server:
	python -m rasa_core.server -d models/dialogue -u models/nlu/default/current -o out_server.log

train:
	python -m rasa_nlu.train --config rouana/config_spacy.yml --data rouana/data/salic_preenchimento.md --path rouana/models/nlu/
	#python bot.py train-dialogue
	python -m rasa_core.train -s rouana/data/rouana_stories.md -d rouana/domain.yml -o models/dialogue --epochs 300
