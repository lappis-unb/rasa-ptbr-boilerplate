build-bot:
	./docker/build-base.sh
	make train

train:
	docker build . -f docker/coach.Dockerfile -t lappis/coach:boilerplate
	docker-compose build bot

run-rocketchat:
	docker-compose up -d rocketchat
	docker-compose up bot

run-telegram:
	docker-compose up telegram_bot

run-console:
	docker-compose run bot make run-console
