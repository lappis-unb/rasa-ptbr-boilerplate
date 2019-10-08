run-telegram:
	rasa run -m /models/dialogue --port 5001 --credentials credentials.yml \
	--endpoints endpoints.yml

run-console:
	rasa shell -m /models/dialogue -vv --cors "*"

run-console-broker:
	rasa shell -m /models/dialogue -vv --endpoints endpoints.yml

run-api:
	rasa run -m /models/dialogue -vv --endpoints endpoints.yml --enable-api

run-actions:
	rasa run actions --actions actions

run-webchat:
	rasa run -m /models/dialogue -vv --endpoints endpoints.yml \
	--credentials credentials.yml --port 5005 --cors '*'
