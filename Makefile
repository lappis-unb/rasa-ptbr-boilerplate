current_dir := $(shell pwd)

first-run:
	make build-bot
	make run-console

build-bot:
	./docker/build-base.sh
	make train

build-analytics:
	docker-compose up -d elasticsearch
	docker-compose up -d rabbitmq
	docker-compose up -d rabbitmq-consumer
	docker-compose up -d kibana
	# This time is a work arround the main objetive is run the following command when elasticsearch is ready
	# The following command is needed just once for project. It's just a setup onfiguration script.
	sleep 30
	docker-compose run --rm -v $(current_dir)/modules/analytics/setup_elastic.py:/analytics/setup_elastic.py bot python /analytics/setup_elastic.py

run-analytics:
	docker-compose up -d rabbitmq
	docker-compose up -d rabbitmq-consumer
	docker-compose up -d elasticsearch
	docker-compose up -d kibana

train:
	docker build . -f docker/coach.Dockerfile -t lappis/coach:boilerplate
	docker-compose build bot

run-validate:
	docker-compose run --rm coach rasa data validate --domain domain.yml --data ./data -vv

run-visualize:
	docker-compose run --rm  -v $(current_dir)/coach:/coach coach rasa visualize --domain domain.yml --stories ./data/stories --config policy_config.yml --nlu ./data/intents --out ./graph.html -vv

run-console:
	docker-compose run bot make run-console

run-webchat:
	docker-compose run -d --rm --service-ports bot make run-webchat
	xdg-open modules/webchat/index.html

run-notebooks:
	docker-compose up -d notebooks
