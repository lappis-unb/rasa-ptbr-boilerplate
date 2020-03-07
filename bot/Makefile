.PHONY: all clean actions

clean:
	rm -rf graph.html results/ models/* *.db*

############################## BOT ############################## 
# RASA X
x:
	rasa x

# NLU
train-nlu:
	rasa train nlu -vv 

# CORE
train:
	rasa train -vv

validate:
	rasa data validate -vv

test:
	rasa test -vv 

# MENSAGEIROS
shell:
	rasa shell -m models/ -vv --endpoints endpoints.yml --port 5004

telegram:
	rasa run -m models/ -vv --port 5001 --credentials credentials.yml \
	--endpoints endpoints.yml

webchat:
	rasa run -m models/ -vv --endpoints endpoints.yml --credentials credentials.yml --port 5005 --cors '*'

api:
	rasa run -m models/ -vv --endpoints endpoints.yml --enable-api

# ACTIONS
actions:
	rasa run actions --actions actions -vv
