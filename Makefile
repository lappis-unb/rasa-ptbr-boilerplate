current_dir := $(shell pwd)

build-bot:
	./docker/build-base.sh
	make train

run-analytics:
	docker-compose up -d rabbitmq
	docker-compose up -d rabbitmq-consumer
	docker-compose up -d elasticsearch
	docker-compose run --rm -v $(current_dir)/modules/analytics:/analytics bot python /analytics/setup_elastic.py
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
	docker-compose run bot make run-webchat

run-notebooks:
	docker-compose up -d notebooks
