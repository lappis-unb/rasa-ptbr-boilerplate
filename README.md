# Rasa Boilerplate
<!-- badges -->
<a href="https://www.gnu.org/licenses/gpl-3.0.pt-br.html"><img src="https://img.shields.io/badge/licence-GPL3-green.svg"/></a>
<a href="https://codeclimate.com/github/lappis-unb/rasa-ptbr-boilerplate/maintainability"><img src="https://api.codeclimate.com/v1/badges/3fe22bf52000e147c6df/maintainability"/></a>


## For English version, see [README-en](docs/README-en.md)

## Tutorial para configurar todo o projeto

Para ter seu chatbot Rasa no ar e funcionando rápidamente no `shell` execute o seguinte comando:

```sh
make first-run
```

Caso ocorra algum erro de permissão, executar o comando `sudo make first-run`.

Este comando irá construir o seu chatbot (containers necessários) e abrir a conversação em um `livechat`
no canto inferior direito da sua tela. Este `mensageiro` é o **WebChat**.

Tudo está dockerizado então você não terá problemas de instalação do ambiente.

## Introdução

Um projeto feito em Rasa com configurações necessárias para a construção de um projeto grande de chatbot.

Este projeto teve como base o projeto [Tais](http://github.com/lappis-unb/tais).

### Entenda a Arquitetura

É utilizado no boilerplate diversas tecnologias que interagem entre si para obter um melhor resultado. Veja a arquitetura implementada:

![](https://user-images.githubusercontent.com/8556291/57933140-d8d66b80-7892-11e9-8d58-a7eda60b099b.png)

O usuário interage com a Boilerplate via Telegram, que manda as mensagens para o Rasa NLU através de
conectores, onde ele identifica a *intent*, e responde pelo Rasa Core, de acordo com as *stories* e *actions*.  
As *models* utilizadas para a conversação foram geradas pelo módulo *trainer* e depois transferidas para o bot, estes
modelos podem ser versionados e evoluídos entre bots.  
Os notebooks avaliam o funcionamento de acordo com o formato das *intents* e *stories*.
O elasticsearch coleta os dados da conversa e armazena para a análise feita pelo kibana, que gera gráficos para
avaliação das conversas dos usuários e do boilerplate.

### Bot

Este script foi configurado para construir as imagens genéricas necessárias para execução deste ambiente.
Caso seu projeto utilize este boilerplate e vá realizar uma integração contínua ou similar, é interessante
criar um repositório para as imagens e substitua os nomes das imagens "lappis/bot", e "lappis/botrequirements" pelas suas respectivas novas imagens, por exemplo "<organização>/bot" em repositório público.


### Treinamento

**Atenção**: o comando de treinamento é usado para criar os modelos necessários na conversação do bot para treinar o seu chatbot execute o comando:

```sh
make train
```

### Console

```sh
make run-shell
```

### Telegram

Após realizar o [tutorial](/docs/setup_telegram.md) de exportação de todas variávies de ambiente necessárias, é possível realizar a execução do bot no telegram corretamente.

**Antes de seguir adiante. Importante:** As variáveis de ambiente são necessárias para o correto funcionamento do bot, por isso não esqueça de exportá-las.

Edite o arquivo **credentials.yml** e descomente as linhas referentes ao telegram:

```sh
telegram:
 access_token: ${TELEGRAM_TOKEN}
 verify: ${TELEGRAM_BOT_USERNAME}
 webhook_url: ${TELEGRAM_WEBHOOK}
```

Se ainda não tiver treinado seu bot execute antes:

```sh
make train
```

Depois execute o bot no telegram:

```sh
make run-telegram
```

### Analytics

Para a visualização dos dados da interação entre o usuário e o chatbot nós utilizamos uma parte da Stack do Elastic, composta pelo ElasticSearch e o Kibana. Com isso, utilizamos um broker para fazer a gerência de mensagens. Então conseguimos adicionar mensagens ao ElasticSearch independente do tipo de mensageiro que estamos utilizando.

### Configuração do RabbitMQ

* Para uma **configuração rápida** execute o seguinte comando:

```sh
make build-analytics
```

O comando acima só precisa ser executado apenas 1 vez e já vai deixar toda a infra de `analytics` pronta para o uso.

Nas próximas vezes que desejar utilizar o `analytics` execute o comando:

```sh
make run-analytics
```

Por fim acesse o **kibana** no `locahost:5601`

* **Explicação completa:**

Em primeiro lugar para fazer o setup do analytics é necessário subir o RabiitMQ e suas configurações.

Inicie o serviço do servidor do RabbitMQ:

```sh
sudo docker-compose up -d rabbitmq
```

Inicie o serviço do consumidor do RabbitMQ, que ficará responsável por enviar as mensagens para o ElasticSearch:

```sh
sudo docker-compose up -d rabbitmq-consumer
```

Lembre-se de configurar as seguintes variáveis de ambiente do serviço `rabbitmq-consumer` no `docker-compose`.

```sh
ENVIRONMENT_NAME=localhost
BOT_VERSION=last-commit-hash
RABBITMQ_DEFAULT_USER=admin
RABBITMQ_DEFAULT_PASS=admin
```

Sendo que as configurações de `RABBITMQ_DEFAULT_USER` e `RABBITMQ_DEFAULT_PASS` devem ser as mesmas definidas no serviço do `rabbitmq`.

#### Integração com Rasa

Existem duas formas para executar a Tais com o *broker*. A primeira delas é via linha de comando.
Para utilizar esta forma é preciso definir Dentro do arquivo `endpoints.yml` as configurações do broker:

```yml
event_broker:
  url: rabbitmq
  username: admin
  password: admin
  queue: bot_messages
```

Ao final é necessário buildar novamente o container do bot.

```
sudo docker-compose up --build -d bot
```

### Configuração ElasticSearch

O ElasticSearch é o serviço responsável por armazenar os dados provenientes da interação entre o usuário e o chatbot.

As mensagens são inseridas no índice do ElasticSearch utilizando o *broker* RabbitMQ.

Para subir o ambiente do ElasticSearch rode os seguintes comandos:

```
sudo docker-compose up -d elasticsearch
sudo docker-compose run --rm -v $PWD/analytics:/analytics bot python /analytics/setup_elastic.py
```

Lembre-se de setar as seguintes variaveis de ambiente no `docker-compose`.

```
ENVIRONMENT_NAME=localhost
BOT_VERSION=last-commit-hash
```

#### Setup Kibana (Visualização)

Para a análise dos dados das conversas com o usuário, utilize o kibana, e veja como os usuários estão interagindo com o bot, os principais assuntos, média de usuários e outras informações da análise de dados.

O Kibana nos auxilia com uma interface para criação de visualização para os dados armazenados nos índices do ElasticSearch.

```sh
sudo docker-compose up -d kibana
```

**Atenção:** Caso queira configurar permissões diferentes de usuários (Login) no ElasticSearch/Kibana, siga esse tutorial ([link](https://github.com/lappis-unb/rasa-ptbr-boilerplate/tree/master/docs/setup_user_elasticsearch.md)).

#### Importação de dashboards

Caso queira subir com os dashboards que criamos para fazer o monitoramento de bots:

```
sudo docker-compose run --rm kibana python3.6 import_dashboards.py
```

Após rodar o comando anterior os dashboards importados estarão presentes no menu management/kibana/Saved Objects.

Você pode acessar o kibana no `locahost:5601`

## Notebooks - Análise de dados

### Setup

Levante o container `notebooks`

```sh
make run-notebooks
```

Acesse o notebook em `localhost:8888`

# Como conseguir ajuda

Parte da documentação técnica do framework da Tais está disponível na
[wiki do repositório](https://github.com/lappis-unb/tais/wiki). Caso não encontre sua resposta, abra uma issue
com a tag `duvida` que tentaremos responder o mais rápido possível.

Em caso de dúvidas em relação ao Rasa, veja o grupo [Telegram Rasa Stack Brasil](https://t.me/RasaBrasil),
estamos lá também para ajudar.

Veja mais informações de contato em nosso site: https://lappis.rocks

# Licença

Todo o framework do boilerplate é desenvolvido sob a licença
[GPL3](https://github.com/lappis-unb/rasa-ptbr-boilerplate/blob/master/LICENSE)

Veja a lista de dependências de licenças [aqui](https://libraries.io/github/lappis-unb/rasa-ptbr-boilerplate)
