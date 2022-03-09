current_dir := $(shell pwd)
user := $(shell whoami)

ENDPOINTS = endpoints/docker-endpoints.yml
CREDENTIALS = credentials/credentials.yml

# CLEAR PROJECT
clean:
	docker-compose down
	cd bot/ && make clean

stop:
	docker-compose stop


# DOCKERHUB
dchub-tag:
	docker tag arthurtemporim/boilerplate arthurtemporim/boilerplate:2.8.12

dchub-push:
	docker push arthurtemporim/boilerplate

# RUN
init:
	make build
	make train
	make shell

build:
	make build-bot

build-requirements:
	docker build . \
		--no-cache \
		-f docker/requirements.Dockerfile \
		-t arthurtemporim/boilerplate

build-bot:
	docker-compose build \
		--no-cache bot

shell:
	docker-compose run \
		--rm \
		--service-ports \
		bot \
		make shell ENDPOINTS=$(ENDPOINTS)

api:
	docker-compose run \
		--rm \
		--service-ports \
		bot \
		make api ENDPOINTS=$(ENDPOINTS) CREDENTIALS=$(CREDENTIALS)

actions:
	docker-compose run \
		--rm \
		--service-ports \
		bot \
		make actions


webchat:
	echo "Executando Bot com Webchat."
	docker-compose run \
		-d \
		--rm \
		--service-ports \
		bot \
		make webchat ENDPOINTS=$(ENDPOINTS) CREDENTIALS=$(CREDENTIALS)
	docker-compose up \
		-d \
		webchat
	echo "Acesse o WEBCHAT em: http://localhost:5010"

telegram:
	docker-compose run \
		-d \
		--rm \
		--service-ports \
		bot-telegram \
		make telegram ENDPOINTS=$(ENDPOINTS) CREDENTIALS=$(CREDENTIALS)

# DEVELOPMENT
x:
	docker-compose run \
		--rm \
		--service-ports \
		x \
		make x
train:
	docker-compose run \
		--rm bot \
		make train

validate:
	docker-compose run \
		--rm bot \
		make validate

test:
	docker-compose run \
		--rm bot \
		make test

test-nlu:
	docker-compose run \
		--rm \
		bot \
		make test-nlu

test-core:
	docker-compose run \
		--rm \
		bot \
		make test-core

