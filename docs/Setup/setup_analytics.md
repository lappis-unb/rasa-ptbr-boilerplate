## Configuração da stack de analytics
Este documento tem por objetivo detalhar o processo de configuração da *stack* de *analytics* utilizada no boilerplate.

Aqui os passos de configuração são descritos separadamente, para facilitar o entendimento e a adaptação. Caso você já tenha executado os comandos `make build-analytics`, `make config-elastic` e `make config-kibana`, não é necessário executar os passos abaixo, e o *analytics* já deve estar funcionando para o seu *bot*.

#### RabbitMQ

###### Configuração do *server* e dos *consumers*
Em primeiro lugar para fazer o setup do analytics é necessário subir o RabbitMQ e definir suas configurações.

Inicie o serviço do servidor do RabbitMQ:

```sh
sudo docker-compose up -d rabbitmq
```

Inicie o serviço do consumidor do RabbitMQ, que ficará responsável por enviar as mensagens para o ElasticSearch:

```sh
sudo docker-compose up -d rabbitmq-consumer
```

Lembre-se de configurar as credenciais de acesso do *server* e dos *consumers* do `rabbitmq`, nos arquivos `env/rabbitmq.env` e `env/rabbitmq-consumer.env`. Estas credenciais devem ser as mesmas, para que estes serviços consigam se integrar corretamente:

```sh
RABBITMQ_DEFAULT_USER=admin
RABBITMQ_DEFAULT_PASS=admin
```

###### Integração com Rasa

Cada mensagem trocada com o *bot* será enviada à uma fila no servidor do *RabbitMQ*, para isso, é precisso integrar esses dois serviços.
Isso é feito definindo as configurações de *broker* do Rasa no arquivo `bot/endpoints.yml`:

```yml
event_broker:
  type: pika
  url: rabbitmq
  username: admin
  password: admin
  queues:
    - bot_messages
```

#### Configuração ElasticSearch

O ElasticSearch é o serviço responsável por armazenar os dados provenientes da interação entre o usuário e o chatbot.

As mensagens são inseridas no índice do ElasticSearch utilizando o *broker* RabbitMQ.

Para subir o ambiente do ElasticSearch rode os seguintes comandos:

```
sudo docker-compose up -d elasticsearch
sudo docker-compose run --rm -v $(pwd)/modules/analytics:/analytics bot python /analytics/setup_elastic.py
```

Lembre-se de setar as seguintes variaveis de ambiente no `docker-compose`.

```
ENVIRONMENT_NAME=localhost
BOT_VERSION=last-commit-hash
```

#### Configuração Kibana (Visualização)

Para a análise dos dados das conversas com o usuário, utilize o kibana, e veja como os usuários estão interagindo com o bot, os principais assuntos, média de usuários e outras informações da análise de dados.

O Kibana nos auxilia com uma interface para criação de visualização para os dados armazenados nos índices do ElasticSearch.

```sh
sudo docker-compose up -d kibana
```

**Atenção:** Caso queira configurar permissões diferentes de usuários (Login) no ElasticSearch/Kibana, siga esse tutorial ([link](https://github.com/lappis-unb/rasa-ptbr-boilerplate/tree/master/docs/setup_user_elasticsearch.md)).

###### Importação de dashboards

Caso queira subir com os dashboards que criamos para fazer o monitoramento de bots:

```
sudo docker-compose run --rm -v $(pwd)/modules/analytics/:/analytics/ kibana python3 /analytics/import_dashboards.py
```

Você pode acessar o kibana na url `localhost:5601`
