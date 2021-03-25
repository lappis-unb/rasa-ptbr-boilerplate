.PHONY: all clean actions

# TODO: This is a hotfix while RASA don't solve dependencies issues.
PIP_FLAGS = --use-deprecated=legacy-resolver 

clean:
	rm -rf graph.html results/ models/* *.db*

install:
	pip install --upgrade pip && \
	pip install $(PIP_FLAGS) -r ../requirements.txt && \
	pip install $(PIP_FLAGS) -r ../x-requirements.txt

# RASA X
x:
	rasa x

# NLU
train-nlu:
	rasa train nlu -vv

# CORE
train:
	rasa train -vv

# TESTS
test:
	rasa test --out results/

test-nlu:
	rasa test nlu --out results/results-nlu-test

test-core:
	rasa test core --fail-on-prediction-errors --out results/results-core-test

# VALIDACAO
validate:
	rasa data validate -vv

# MENSAGEIROS
shell:
	rasa shell -m models/ -vv --endpoints endpoints.yml --port 5006

telegram:
	rasa run -m models/ -vv --port 5001 --credentials credentials.yml \
	--endpoints endpoints.yml

webchat:
	rasa run -m models/ -vv --endpoints endpoints.yml --credentials credentials.yml --port 5007 --cors '*'

api:
	rasa run -m models/ -vv --endpoints endpoints.yml --enable-api --port 5006

rocket:
	python /modules/rocketchat/bot_config.py
	rasa run -m models/ -vv --endpoints endpoints.yml --credentials credentials.yml --port 5005 --cors '*'


# ACTIONS
actions:
	rasa run actions --actions actions -vv
