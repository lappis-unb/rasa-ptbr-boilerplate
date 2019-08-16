build:
	./docker/build-base.sh
	make train

train:
	docker-compose rm -s -f coach
	docker-compose build coach

run-telegram:
	docker-compose up telegram_bot

run-console:
	docker-compose run --rm bot make run-console

run-api:
	docker-compose run --rm bot make run-api