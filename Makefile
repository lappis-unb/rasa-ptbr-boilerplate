current_dir := $(shell pwd)

clean:
	sudo docker-compose down

############################## BOILERPLATE ############################## 
first-run:
	sudo make build
	make run-webchat

build:
	make build-requirements
	make build-coach
	make build-bot

build-requirements:
	docker build . -f docker/requirements.Dockerfile -t botrequirements

build-bot:
	sudo docker-compose build bot
	
build-coach:
	sudo docker-compose up coach

build-analytics:
	sudo docker-compose up -d elasticsearch
	sudo docker-compose up -d rabbitmq
	sudo docker-compose up -d rabbitmq-consumer
	sudo docker-compose up -d kibana
	# This sleep time is a work arround the main objetive is run the following command when elasticsearch is ready
	# The following command is needed just once for project. It's just a setup onfiguration script.
	sleep 30
	sudo docker-compose run --rm -v $(current_dir)/modules/analytics/setup_elastic.py:/analytics/setup_elastic.py bot python /analytics/setup_elastic.py
	sudo docker-compose run --rm -v $(current_dir)/modules/analytics/:/analytics/ bot python /analytics/import_dashboards.py
	echo "Não se esqueça de atualizar o arquivo endpoints.yml"
	sensible-browser --no-sandbox http://localhost:5601

run-analytics:
	sudo docker-compose up -d rabbitmq
	sudo docker-compose up -d rabbitmq-consumer
	sudo docker-compose up -d elasticsearch
	sudo docker-compose up -d kibana
	sensible-browser --no-sandbox http://localhost:5601

run-shell:
	sudo docker-compose run --rm --service-ports bot make shell

run-webchat:
	sudo docker-compose run -d --rm --service-ports bot-webchat
	sensible-browser modules/webchat/index.html

run-telegram:
	sudo docker-compose run -d --rm --service-ports bot_telegram make telegram

run-notebooks:
	sudo docker-compose up -d notebooks
	sensible-browser --no-sandbox http://localhost:8888

train:
	sudo docker-compose up coach
	sudo docker-compose build bot

validate:
	sudo docker-compose run --rm coach rasa data validate --domain domain.yml --data data/ -vv

visualize:
	sudo docker-compose run --rm  -v $(current_dir)/bot:/coach coach rasa visualize --domain domain.yml --stories data/stories.md --config config.yml --nlu data/nlu.md --out ./graph.html -vv
	sensible-browser --no-sandbox bot/graph.html
