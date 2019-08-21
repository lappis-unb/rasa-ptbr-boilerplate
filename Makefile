
build-requirements:
	./docker/build-base.sh

build-coach:
	docker-compose build coach

build-bot:
	docker-compose build bot

build:
	make build-requirements
	make build-coach
	make build-bot

first-run:
	make build
	make run-console

train:
	docker-compose rm -s -f coach
	docker-compose build coach

run-telegram:
	docker-compose up telegram_bot

run-console:
	docker-compose run --rm bot make run-console

run-api:
	docker-compose run --rm bot make run-api