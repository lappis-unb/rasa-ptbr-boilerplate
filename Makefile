first-run:
	docker-compose up -d rocketchat
	make build-bot
	docker-compose run --rm bot make config-rocket
	docker-compose up bot

build-bot:
	cd docker && ./build-base.sh
	make train

train:
	docker build . -f docker/coach.Dockerfile -t botcoach:latest
	docker-compose build bot

run-rocketchat:
	docker-compose up -d rocketchat
	docker-compose up bot

run-telegram:
	docker-compose up telegram_bot

run-console:
	docker-compose run bot make run-console
