current_dir := $(shell pwd)

############################## BOILERPLATE ############################## 
first-run:
	make build
	make run-webchat

build:
	make build-requirements
	make build-coach
	make build-bot

build-requirements:
	docker build . -f docker/requirements.Dockerfile -t lappis/botrequirements:boilerplate

build-bot:
	docker-compose build bot
	
build-coach:
	docker-compose build coach

build-analytics:
	docker-compose up -d elasticsearch
	docker-compose up -d rabbitmq
	docker-compose up -d rabbitmq-consumer
	docker-compose up -d kibana
	# This time is a work arround the main objetive is run the following command when elasticsearch is ready
	# The following command is needed just once for project. It's just a setup onfiguration script.
	sleep 30
	docker-compose run --rm -v $(current_dir)/modules/analytics/setup_elastic.py:/analytics/setup_elastic.py bot python /analytics/setup_elastic.py
	docker-compose run --rm -v $(current_dir)/modules/analytics/:/analytics/ bot python /analytics/import_dashboards.py
	echo "Não se esqueça de atualizar o arquivo endpoints.yml"
	#sensible-browser --no-sandbox http://localhost:5601

run-analytics:
	docker-compose up -d rabbitmq
	docker-compose up -d rabbitmq-consumer
	docker-compose up -d elasticsearch
	docker-compose up -d kibana
	#sensible-browser --no-sandbox http://localhost:5601

validate:
	docker-compose run --rm coach rasa data validate --domain domain.yml --data data/ -vv

visualize:
	docker-compose run --rm  -v $(current_dir)/bot:/coach coach rasa visualize --domain domain.yml --stories data/stories.md --config config.yml --nlu data/nlu.md --out ./graph.html -vv
	#sensible-browser --no-sandbox bot/graph.html

run-console:
	docker-compose run bot make console

run-webchat:
	docker-compose run -d --rm --service-ports bot make webchat

run-telegram:
	docker-compose run -d --rm --service-ports bot make telegram

run-notebooks:
	docker-compose up -d notebooks
	#sensible-browser --no-sandbox http://localhost:8888


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
	--out /src_models

coach-train:
	rasa train -vv --out /src_models

train:
	docker build . -f docker/coach.Dockerfile -t lappis/coach:boilerplate
	docker-compose build bot

############################## BOT ############################## 
console:
	rasa shell -m /models/ -vv --endpoints endpoints.yml --cors "*"

console-broker:
	rasa shell -m /models/ -vv --endpoints endpoints.yml

telegram:
	rasa run -m /models/ --port 5001 --credentials credentials.yml \
	--endpoints endpoints.yml

webchat:
	rasa run -m /models/ -vv --endpoints endpoints.yml \
	--credentials credentials.yml --port 5005 --cors '*'

run-api:
	rasa run -m /models/ -vv --endpoints endpoints.yml --enable-api

############################## ACTIONS ############################## 
run-actions:
	rasa run actions --actions actions
