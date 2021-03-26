current_dir := $(shell pwd)
user := $(shell whoami)

clean:
	docker-compose down
	cd bot/ && make clean

stop:
	docker-compose stop

############################## BOILERPLATE ##############################
first-run:
	make build
	make train
	make run-shell

build:
	make build-requirements
	make build-coach
	make build-bot

build-requirements:
	docker build . \
		--no-cache \
		-f docker/requirements.Dockerfile \
		-t botrequirements

build-bot:
	docker-compose build \
		--no-cache bot

build-coach:
	docker-compose build \
		--no-cache coach

build-analytics:
	make run-analytics
	make config-elastic
	# This line should be removed ASAP
	sleep 10
	# Run this command only when kibana is up and ready. A script is needed.
	make config-kibana

config-elastic:
	docker-compose run \
		--rm \
		-v $(current_dir)/modules/analytics/setup_elastic.py:/analytics/setup_elastic.py \
		bot \
		python /analytics/setup_elastic.py

config-kibana:
	docker-compose run \
		--rm \
		-v $(current_dir)/modules/analytics/:/analytics/ \
		kibana \
		python3 /analytics/import_dashboards.py
	echo "Acesse o KIBANA em: http://localhost:5601"

run-analytics:
	docker-compose up \
		-d elasticsearch
	docker-compose up \
		-d rabbitmq
	docker-compose up \
		-d rabbitmq-consumer
	docker-compose up \
		-d kibana

run-shell:
	docker-compose run \
		--rm \
		--service-ports \
		bot \
		make shell

run-api:
	docker-compose run \
		--rm \
		--service-ports \
		bot \
		make api

run-actions:
	docker-compose run \
		--rm \
		--service-ports \
		bot \
		make actions

run-x:
	docker-compose run \
		--rm \
		--service-ports \
		x \
		make x

run-webchat:
	echo "Executando Bot com Webchat."
	docker-compose run \
		-d \
		--rm \
		--service-ports \
		bot-webchat
	docker-compose up \
		-d \
		webchat
	echo "Acesse o WEBCHAT em: http://localhost:5010"

run-telegram:
	docker-compose run \
		-d \
		--rm \
		--service-ports \
		bot_telegram \
		make telegram

run-notebooks:
	docker-compose up \
		-d notebooks
	echo "Acesse o KIBANA em: http://localhost:8888"

run-rocket:
	docker-compose up \
		-d rocketchat \
		bot-rocket
	echo "Acesse o ROCKETCHAT em: http://localhost:5003"

train:
	mkdir -p bot/models
	docker-compose up \
		--build coach

############################## TESTS ##############################
test:
	docker-compose run \
		--rm bot \
		make test

run-test-nlu:
	docker-compose run \
		--rm \
		bot \
		make test-nlu

run-test-core:
	docker-compose run \
		--rm \
		bot \
		make test-core

