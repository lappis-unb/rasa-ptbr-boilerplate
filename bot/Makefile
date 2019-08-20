run-rocketchat:
	make config-bot
	python3 run-rocketchat.py

run-telegram:
	python -m rasa_core.run -d /models/dialogue -u /models/nlu/current --port 5001 --credentials credentials.yml --endpoints endpoints.yml

config-rocket:
	python /scripts/bot_config.py

run-console:
	python3 -m rasa_core.run -d /models/dialogue -u /models/nlu/current --debug

run-console-broker:
	python3 -m rasa_core.run -d /models/dialogue -u /models/nlu/current --debug --endpoints endpoints.yml

run-api:
	python3 -m rasa_core.run -d /models/dialogue -u /models/nlu/current \
  --endpoints endpoints.yml --debug --enable_api 

evaluate:
	python3 -m rasa_core.evaluate -d /models/dialogue -s data/core/

run-actions:
	python -m rasa_core_sdk.endpoint --actions actions

# Force Makefile to execute e2e command every time
.PHONY: all e2e clean
test-dialogue:
	make e2e

e2e:
	python3 -m rasa_core.evaluate default --core /models/dialogue --nlu /models/nlu/current --stories e2e/e2e_stories.md --e2e

test-stories:
	python3 test_stories.py --stories e2e/e2e_stories.md --e2e

config-bot:
	python /scripts/bot_config.py -r ${ROCKETCHAT_URL} -an ${ROCKETCHAT_ADMIN_USERNAME} -ap ${ROCKETCHAT_ADMIN_PASSWORD} -bu ${ROCKETCHAT_BOT_USERNAME} -bp ${ROCKETCHAT_BOT_PASSWORD}
