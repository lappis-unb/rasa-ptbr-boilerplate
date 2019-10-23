clean:
	rm -rf graph.html results/ models/*

############################## BOT ############################## 
# NLU
train-nlu:
	rasa train nlu -vv 

test-nlu:
	rasa test nlu -vv 

# CORE
train:
	rasa train -vv --out models/

# MENSAGEIROS
shell:
	rasa shell -m models/ -vv --endpoints endpoints.yml --port 5004 --cors "*"

telegram:
	rasa run -m models/ -vv --port 5001 --credentials credentials.yml \
	--endpoints endpoints.yml

webchat:
	rasa run -m models/ -vv --endpoints endpoints.yml --credentials credentials.yml --port 5005 --cors '*'

run-api:
	rasa run -m models/ -vv --endpoints endpoints.yml --enable-api

# ACTIONS
run-actions:
	rasa run actions --actions actions -vv
