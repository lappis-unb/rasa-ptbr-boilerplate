current_dir := $(shell pwd)

############################## BOILERPLATE ############################## 
first-run:
	make build-bot
	make run-webchat

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
	docker-compose run --rm kibana python3.6 $(current_dir)/modules/analytics/import_dashboards.py

run-analytics:
	docker-compose up -d rabbitmq
	docker-compose up -d rabbitmq-consumer
	docker-compose up -d elasticsearch
	docker-compose up -d kibana

validate:
	docker-compose run --rm coach rasa data validate --domain bot/domain.yml --data ./bot/data -vv

visualize:
	docker-compose run --rm  -v $(current_dir)/bot:/coach coach rasa visualize --domain bot/domain.yml --stories ./bot/data/stories.md --config bot/config.yml --nlu ./bot/data/nlu.md --out ./graph.html -vv

run-console:
	docker-compose run bot make run-console

run-webchat:
	docker-compose run -d --rm --service-ports bot make webchat
	sensible-browser --no-sandbox modules/webchat/index.html

run-notebooks:
	docker-compose up -d notebooks


############################## COACH ############################## 
train-nlu:
	rasa train nlu -vv         \
	--config config.yml        \
	--fixed-model-name current \
	--nlu data/                \
	--out /src_models

train-core:
	rasa train core -vv     \
	--config config.yml     \
	-d domain.yml           \
	-s data/                \
	--out /src_models/dialogue/

coach-train: train-nlu train-core

train:
	docker build . -f docker/coach.Dockerfile -t lappis/coach:boilerplate
	docker-compose build bot


############################## BOT ############################## 
console:
	rasa shell -m /models/dialogue -vv --cors "*"

console-broker:
	rasa shell -m /models/dialogue -vv --endpoints endpoints.yml

telegram:
	rasa run -m /models/dialogue --port 5001 --credentials credentials.yml \
	--endpoints endpoints.yml

webchat:
	rasa run -m /models/dialogue -vv --endpoints endpoints.yml \
	--credentials credentials.yml --port 5005 --cors '*'

run-api:
	rasa run -m /models/dialogue -vv --endpoints endpoints.yml --enable-api


############################## ACTIONS ############################## 
run-actions:
	rasa run actions --actions actions
