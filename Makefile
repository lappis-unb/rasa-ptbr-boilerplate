current_dir := $(shell pwd)

clean:
	docker-compose down

stop:
	docker-compose stop

############################## BOILERPLATE ##############################
first-run:
	make build
	make train
	make run-shell

build:
	make build-requirements
	make build-coach
	make build-bot

build-requirements:
	docker build . --no-cache -f docker/requirements.Dockerfile -t botrequirements

build-bot:
	docker-compose build --no-cache bot

build-coach:
	docker-compose build --no-cache coach

build-analytics:
	docker-compose up -d elasticsearch
	docker-compose up -d rabbitmq
	docker-compose up -d rabbitmq-consumer
	docker-compose up -d kibana
	# This sleep time is a work arround the main objetive is run the following command when elasticsearch is ready
	# The following command is needed just once for project. It's just a setup onfiguration script.
	sleep 30
	docker-compose run --rm -v $(current_dir)/modules/analytics/setup_elastic.py:/analytics/setup_elastic.py bot python /analytics/setup_elastic.py
	docker-compose run --rm -v $(current_dir)/modules/analytics/:/analytics/ bot python /analytics/import_dashboards.py
	$(info )
	$(info Não se esqueça de atualizar o arquivo endpoints.yml)
	$(info )
	sensible-browser --no-sandbox http://localhost:5601

run-analytics:
	docker-compose up -d rabbitmq
	docker-compose up -d rabbitmq-consumer
	docker-compose up -d elasticsearch
	docker-compose up -d kibana
	sensible-browser --no-sandbox http://localhost:5601

run-shell:
	docker-compose run --rm --service-ports bot make shell

run-x:
	docker-compose run --rm --service-ports bot make x

run-webchat:
	$(info )
	$(info Executando Bot com Webchat. Caso seu navegador não seja iniciado automáticamente, abra o seguinte arquivo com seu navegador: modules/webchat/index.html)
	$(info )
	docker-compose run -d --rm --service-ports bot-webchat
	sensible-browser modules/webchat/index.html

run-telegram:
	docker-compose run -d --rm --service-ports bot_telegram make telegram

run-notebooks:
	docker-compose up -d notebooks
	sensible-browser --no-sandbox http://localhost:8888

train:
	mkdir -p bot/models
	docker-compose up --build coach

############################## TESTS ##############################
run-test-nlu:
	docker-compose run --rm bot make test-nlu

run-test-core:
	docker-compose run --rm bot make test-core

validate:
	docker-compose run --rm coach rasa data validate --domain domain.yml --data data/ -vv

visualize:
	docker-compose run --rm  -v $(current_dir)/bot:/coach coach rasa visualize --domain domain.yml --stories data/stories.md --config config.yml --nlu data/nlu.md --out ./graph.html -vv
	sensible-browser --no-sandbox bot/graph.html
