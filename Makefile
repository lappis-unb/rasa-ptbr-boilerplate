build-requirements:
	docker build . -f docker/requirements.Dockerfile -t lappis/botrequirements:boilerplate

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
	docker build . -f docker/coach.Dockerfile -t lappis/coach:boilerplate
	docker-compose build bot

run-telegram:
	docker-compose up telegram_bot

run-console:
	docker-compose run --rm bot make run-console

run-rocketchat:
	docker-compose up -d rocketchat
	sleep 25
	docker-compose up -d bot

test-dialogue:
	docker-compose run --rm bot make e2e