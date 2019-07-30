build-bot:
	./docker/build-base.sh
	make train

train:
	docker build . -f docker/coach.Dockerfile -t lappis/coach:boilerplate
	docker-compose build bot

run-rocketchat:
	make config-bot
	python3 run-rocketchat.py

run-telegram:
	docker-compose up telegram_bot

run-console:
	docker-compose run bot make run-console

config-bot:
	python /scripts/bot_config.py -r ${ROCKETCHAT_URL} -an ${ROCKETCHAT_ADMIN_USERNAME} -ap ${ROCKETCHAT_ADMIN_PASSWORD} -bu ${ROCKETCHAT_BOT_USERNAME} -bp ${ROCKETCHAT_BOT_PASSWORD}
