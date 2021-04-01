.PHONY: all clean actions

## FLAGS:
# TODO: This is a hotfix while RASA don't solve dependencies issues.
PIP_FLAGS = --use-deprecated=legacy-resolver 
LOG_LEVEL = -v
RASA_ENDPOINTS = --endpoints endpoints.yml
RASA_CREDENTIALS = --credentials credentials.yml

clean:
	rm -rf graph.html results/ models/* *.db*

install:
	pip install --upgrade pip 						&& \
	pip install $(PIP_FLAGS) -r requirements.txt	&& \
	pip install $(PIP_FLAGS) -r x-requirements.txt

# RASA X
x:
	rasa x

# NLU
train-nlu:
	rasa train nlu 			\
		$(LOG_LEVEL)

# CORE
train:
	rasa train 				\
		$(LOG_LEVEL)

# TESTS
test:
	rasa test 				\
		--out results/

test-nlu:
	rasa test nlu 			\
		--out results/results-nlu-test

test-core:
	rasa test core 						\
		--fail-on-prediction-errors 	\
		--out results/results-core-test

# UTIL
validate:
	rasa data validate 		\
		$(LOG_LEVEL)

visualize:
		rasa visualize 		\
			--out ./graph.html

# CHAT
shell:
	rasa shell 				\
		-m models/ 			\
		$(LOG_LEVEL)		\
		$(RASA_ENDPOINTS)	\
		--port 5006

telegram:
	rasa run 				\
		-m models/ 			\
		$(LOG_LEVEL) 		\
		$(RASA_ENDPOINTS)	\
		$(RASA_CREDENTIALS)	\
		--port 5001 		\

webchat:
	rasa run 				\
		-m models/ 			\
		$(LOG_LEVEL) 		\
		$(RASA_ENDPOINTS)	\
		$(RASA_CREDENTIALS)	\
		--port 5007 

api:
	rasa run 				\
		-m models/ 			\
		$(LOG_LEVEL) 		\
		$(RASA_ENDPOINTS)	\
		--enable-api 		\
		--cors '*'			\
		--port 5006

rocket:
	python /modules/rocketchat/bot_config.py
	rasa run 				\
		-m models/ 			\
		$(LOG_LEVEL) 		\
		$(RASA_ENDPOINTS)	\
		$(RASA_CREDENTIALS)	\
		--cors '*' 			\
		--port 5005 


# ACTIONS
actions:
	rasa run actions 		\
		--actions actions 	\
		$(LOG_LEVEL)
