current_dir := $(shell pwd)
user := $(shell whoami)

clean:
	docker-compose down
	cd bot/ && make clean

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
	make config-elastic
	make config-kibana

config-elastic:
	docker-compose run --rm -v $(current_dir)/modules/analytics/setup_elastic.py:/analytics/setup_elastic.py bot python /analytics/setup_elastic.py

config-kibana:
	docker-compose run --rm -v $(current_dir)/modules/analytics/:/analytics/ kibana python3 /analytics/import_dashboards.py
	$(info )
	$(info Acesse o KIBANA em: http://localhost:5601)
	$(info )

run-shell:
	docker-compose run --rm --service-ports bot make shell

run-api:
	docker-compose run --rm --service-ports bot make api

run-actions:
	docker-compose run --rm --service-ports bot make actions

run-x:
	docker-compose run --rm --service-ports bot make x

run-webchat:
	$(info )
	$(info Executando Bot com Webchat.)
	$(info )
	docker-compose run -d --rm --service-ports bot-webchat
	$(info )
	$(info Caso o FIREFOX não seja iniciado automáticamente, abra o seguinte arquivo com seu navegador:)
	$(info modules/webchat/index.html)
	$(info )
	firefox modules/webchat/index.html

run-telegram:
	docker-compose run -d --rm --service-ports bot_telegram make telegram

run-notebooks:
	docker-compose up -d notebooks
	$(info )
	$(info Acesse o KIBANA em: http://localhost:8888)
	$(info )

train:
	mkdir -p bot/models
	docker-compose up --build coach

############################## TESTS ##############################
test:
	docker-compose run --rm bot make test

run-test-nlu:
	docker-compose run --rm bot make test-nlu

run-test-core:
	docker-compose run --rm bot make test-core

validate:
	docker-compose run --rm bot rasa data validate --domain domain.yml --data data/ -vv

visualize:
	docker-compose run --rm  -v $(current_dir)/bot:/coach coach rasa visualize --domain domain.yml --stories data/stories.md --config config.yml --nlu data/nlu.md --out ./graph.html -vv
	$(info )
	$(info Caso o FIREFOX não seja iniciado automáticamente, abra o seguinte arquivo com seu navegador:)
	$(info bot/graph.html)
	firefox bot/graph.html
