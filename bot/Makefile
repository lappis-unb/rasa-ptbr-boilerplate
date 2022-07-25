.PHONY: all clean actions

## FLAGS:
# TODO: This is a hotfix while RASA don't solve dependencies issues.
PIP_FLAGS = --use-deprecated=legacy-resolver
LOG_LEVEL = -v
RASA_ENDPOINTS = --endpoints 
ENDPOINTS = endpoints.yml
RASA_CREDENTIALS = --credentials
CREDENTIALS = credentials.yml

# CLEAN PROJECT
clean:
	rm -rf graph.html results/ models/* *.db* .*tensorboard*

install:
	pip install --upgrade pip 						&& \
	pip install -r requirements.txt

# RUN
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
		--port 5005

webchat:
	rasa run \
		-m models/ \
		$(LOG_LEVEL) \
		$(RASA_ENDPOINTS) $(ENDPOINTS) \
		$(RASA_CREDENTIALS) $(CREDENTIALS) \
		--cors '*' \
		--port 5005 

telegram:
	rasa run \
		-m models/ \
		$(LOG_LEVEL) \
		$(RASA_ENDPOINTS) $(ENDPOINTS) \
		$(RASA_CREDENTIALS)	credentials/telegram-credentials.yml \
		--port 5005 \

# ACTIONS
actions:
	rasa run actions \
		--actions actions \
		$(LOG_LEVEL)

# DEVELOPMENT
train-nlu:
	rasa train nlu \
		$(LOG_LEVEL)

train:
	rasa train \
		$(LOG_LEVEL)

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
## RASA X
install-x:
	pip install -r x-requirements.txt

x:
	rasa x --no-prompt

## RASALIT
install-rasalit:
	pip install $(PIP_FLAGS) -r rasalit-requirements.txt

rasalit:
	python -m rasalit nlu-cluster --port 8501

interactive:
	rasa interactive

validate:
	rasa data validate \
		$(LOG_LEVEL)

visualize:
		rasa visualize \
			--out ./graph.html

tensor:
		tensorboard \
			--logdir .

