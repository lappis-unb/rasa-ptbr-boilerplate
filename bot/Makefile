.PHONY: all clean actions

## FLAGS:
# TODO: This is a hotfix while RASA don't solve dependencies issues.
PIP_FLAGS = --use-deprecated=legacy-resolver
LOG_LEVEL = -v
RASA_ENDPOINTS = --endpoints 
ENDPOINTS = endpoints/endpoints.yml
RASA_CREDENTIALS = --credentials
CREDENTIALS = credentials/credentials.yml

clean:
	rm -rf graph.html results/ models/* *.db*

install:
	pip install --upgrade pip 						&& \
	pip install $(PIP_FLAGS) -r requirements.txt

# RASA X
install-x:
	pip install $(PIP_FLAGS) -r x-requirements.txt

x:
	rasa x

# RASALIT
install-rasalit:
	pip install $(PIP_FLAGS) -r rasalit-requirements.txt

rasalit:
	python -m rasalit nlu-cluster --port 8501

# NLU
train-nlu:
	rasa train nlu \
		$(LOG_LEVEL)

# CORE
train:
	rasa train \
		$(LOG_LEVEL)

# TESTS
test:
	rasa test \
		--out results/

test-nlu:
	rasa test nlu \
		--out results/results-nlu-test

test-core:
	rasa test core \
		--fail-on-prediction-errors \
		--out results/results-core-test

# UTIL
interactive:
	rasa interactive

validate:
	rasa data validate \
		$(LOG_LEVEL)

visualize:
		rasa visualize \
			--out ./graph.html

tensor_diet:
		tensorboard \
			--logdir .tensorboard_diet

tensor_ted:
		tensorboard \
			--logdir .tensorboard_ted

# CHAT
api:
	rasa run \
		-m models/ \
		$(LOG_LEVEL) \
		$(RASA_ENDPOINTS) $(ENDPOINTS) \
		$(RASA_CREDENTIALS)	$(CREDENTIALS) \
		--enable-api \
		--cors '*' \
		--port 5005

shell:
	rasa shell \
		-m models/ \
		$(LOG_LEVEL) \
		$(RASA_ENDPOINTS) $(ENDPOINTS) \
		--port 5006

webchat:
	rasa run \
		-m models/ \
		$(LOG_LEVEL) \
		$(RASA_ENDPOINTS) $(ENDPOINTS) \
		$(RASA_CREDENTIALS)	$(CREDENTIALS) \
		--cors '*' \
		--port 5007 

telegram:
	rasa run \
		-m models/ \
		$(LOG_LEVEL) \
		$(RASA_ENDPOINTS) $(ENDPOINTS) \
		$(RASA_CREDENTIALS)	credentials/telegram-credentials.yml \
		--port 5008 \

rocket:
	python /modules/rocketchat/bot_config.py
	rasa run \
		-m models/ \
		$(LOG_LEVEL) \
		$(RASA_ENDPOINTS) $(ENDPOINTS) \
		$(RASA_CREDENTIALS)	credentials/rocketchat-credentials.yml \
		--cors '*' \
		--port 5009


# ACTIONS
actions:
	rasa run actions \
		--actions actions \
		$(LOG_LEVEL)
