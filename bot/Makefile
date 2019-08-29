run-rocketchat:
	make config-bot
	python3 run_rocketchat.py

run-telegram:
	rasa run -m /models/dialogue --port 5001 --credentials credentials.yml \
	--endpoints endpoints.yml

config-rocket:
	python /scripts/bot_config.py

run-console:
	rasa shell -m /models/dialogue -vv

run-console-broker:
	rasa shell -m /models/dialogue -vv --endpoints endpoints.yml

run-api:
	rasa run -m /models/dialogue -vv --endpoints endpoints.yml --enable_api 

run-actions:
	rasa run actions --actions actions

# Force Makefile to execute e2e command every time
#.PHONY: all e2e clean
#test-dialogue:
#	make e2e
#
#e2e:
#	python3 -m rasa_core.evaluate default --core /models/dialogue --nlu /models/nlu/current --stories e2e/e2e_stories.md --e2e
#
#test-stories:
#	python3 test_stories.py --stories e2e/e2e_stories.md --e2e
#
#config-bot:
#	python /scripts/bot_config.py -r ${ROCKETCHAT_URL} -an ${ROCKETCHAT_ADMIN_USERNAME} -ap ${ROCKETCHAT_ADMIN_PASSWORD} -bu ${ROCKETCHAT_BOT_USERNAME} -bp ${ROCKETCHAT_BOT_PASSWORD}
