run-telegram:
	rasa run -m /models/dialogue --port 5001 --credentials credentials.yml \
	--endpoints endpoints.yml

run-console:
	rasa shell -m /models/dialogue -vv

run-console-broker:
	rasa shell -m /models/dialogue -vv --endpoints endpoints.yml

run-api:
	rasa run -m /models/dialogue -vv --endpoints endpoints.yml --enable_api 

run-actions:
	rasa run actions --actions actions

run-webchat:
	rasa run -m /models/dialogue -vv --endpoints endpoints.yml \
	--credentials credentials.yml --port 5005 --cors '*'

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
