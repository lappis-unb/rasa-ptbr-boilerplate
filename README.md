# Rasa Boilerplate
<!-- badges -->
<a href="https://www.gnu.org/licenses/gpl-3.0.pt-br.html"><img src="https://img.shields.io/badge/licence-GPL3-green.svg"/></a>
<a href="https://codeclimate.com/github/lappis-unb/rasa-ptbr-boilerplate/maintainability"><img src="https://api.codeclimate.com/v1/badges/3fe22bf52000e147c6df/maintainability"/></a>

### For English version, see [README-en](docs/README-en.md)

Um projeto feito em Rasa com configurações necessárias para a construção de um projeto grande de chatbot.

Este projeto teve como base a [Tais](http://github.com/lappis-unb/tais).

# Entenda a Arquitetura

É utilizado no boilerplate diversas tecnologias que interagem entre si para obter um melhor resultado. Veja a arquitetura implementada:

![](https://user-images.githubusercontent.com/8556291/57933140-d8d66b80-7892-11e9-8d58-a7eda60b099b.png)

O usuário interage com a Boilerplate via RocketChat ou Telegram, que manda as mensagens para o Rasa NLU através de
conectores, onde ele identifica a *intent*, e responde pelo Rasa Core, de acordo com as *stories* e *actions*.  
As *models* utilizadas para a conversação foram geradas pelo módulo *trainer* e depois transferidas para o bot, estes
modelos podem ser versionados e evoluídos entre bots.  
Os notebooks avaliam o funcionamento de acordo com o formato das *intents* e *stories*.
O elasticsearch coleta os dados da conversa e armazena para a análise feita pelo kibana, que gera gráficos para
avaliação das conversas dos usuários e do boilerplate.

## Bot


Este script foi configurado para construir as imagens genéricas necessárias para execução deste ambiente.
Caso seu projeto utilize este boilerplate e vá realizar uma integração contínua ou similar, é interessante
criar um repositório para as imagens e substitua os nomes das imagens "lappis/bot", "lappis/coach" e "lappis/botrequirements" pelas
suas respectivas novas imagens, por exemplo "<organização>/bot" em repositório público.

### RocketChat
Para testar o assistente virtual utilizando da plataforma do RocketChat, siga os seguintes comandos para subir os containers em seu computador:


```sh
sudo docker-compose up -d rocketchat

# Caso não vá subir a stack do Analytics
# aguarde o container do rocketchat subir
sudo docker-compose up -d bot
```

Caso queira subir toda a stack e vá utilizar do analytics é necessário substituir a seguinte variável de ambiente no `docker/bot-rocketchat.env` de **False** para **True**.
```
# Analytics config
ENABLE_ANALYTICS=True

# E logo após trocar, subir o container do bot
sudo docker-compose up -d bot
```


Após esses comandos o RocketChat deve estar disponível na porta 3000 do seu computador. Entre em http://localhost:3000 para acessar. Será pedido que faça login. Por padrão é gerado um usuário admin: username: admin senha: admin. Nas próximas telas apenas clique na opção `Continue` e `Go to your workspace`.

Para configurar o bot no rocketchat e conseguir conversar com ele pelo próprio rocket, acesse o [link](http://github.com/lappis-unb/rasa-ptbr-boilerplate/tree/master/docs/add_bot_rocketchat.md).


Opcionalmente, é possível fazer uma configuração para que o assistente virtual inicie a conversa, para isso você deve criar um `trigger`.
Para criar um `trigger` entre no rocketchat como `admin`, e vá no painel do Livechat na
seção de Triggers, clique em `New Trigger`. Preencha o Trigger da seguinte forma:


```yaml
Enabled: Yes
Name: Start Talk
Description: Start Talk
Condition: Visitor time on site
    Value: 3
Action: Send Message
 Value: Impersonate next agent from queue
 Value: Olá!
```


#### Instalação

Para executar o bot em um site você precisa inserir o seguinte Javascript na sua página

```js
<!-- Start of Rocket.Chat Livechat Script -->
<script type="text/javascript">
// !!! Mudar para o seu host AQUI !!!
host = 'http://localhost:3000';
// !!! ^^^^^^^^^^^^^^^^^^^^^^^^^^ !!!
(function(w, d, s, u) {
    w.RocketChat = function(c) { w.RocketChat._.push(c) }; w.RocketChat._ = []; w.RocketChat.url = u;
    var h = d.getElementsByTagName(s)[0], j = d.createElement(s);
    j.async = true; j.src = host + '/packages/rocketchat_livechat/assets/rocketchat-livechat.min.js?_=201702160944';
    h.parentNode.insertBefore(j, h);
})(window, document, 'script', host + '/livechat');
</script>
<!-- End of Rocket.Chat Livechat Script -->
```

**Atenção**: Você precisa alterar a variavel `host` dentro do código acima para a url do site onde estará o seu Rocket.Chat.

### Telegram

Após realizar o [tutorial](/docs/setup_telegram.md) de exportação de todas variávies de ambiente necessárias, é possível realizar a execução do bot no telegram corretamente.

<strong><em>Antes de seguir adiante. Importante:</strong></em> As variáveis de ambiente são necessárias para o correto funcionamento do bot, por isso não esqueça de exportá-las.

Se ainda não tiver treinado seu bot execute antes:

```sh
make train
```
**Atenção**: o comando "make train" executa um container docker, caso precise de sudo em seu computador
para execução docker, utilize "sudo make train".  


Depois execute o bot no telegram:

```sh
sudo docker-compose up bot_telegram
```

### Console

```sh
make train
sudo docker-compose run --rm bot make run-console
```

### Train Online

```
make train
sudo docker-compose run --rm coach make train-online
```

## Analytics

Para a visualização dos dados da interação entre o usuário e o chatbot nós utilizamos uma parte da Stack do Elastic, composta pelo ElasticSearch e o Kibana. Com isso, utilizamos um broker para fazer a gerência de mensagens. Então conseguimos adicionar mensagens ao ElasticSearch independente do tipo de mensageiro que estamos utilizando.

#### Setup RabbitMQ

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



### Execução

Existem duas formas para executar a Tais com o *broker*. A primeira delas é via linha de comando.
Para utilizar esta forma é preciso definir Dentro do arquivo `endpoints.yml` as configurações do broker:

```yml
event_broker:
  url: rabbitmq
  username: admin
  password: admin
  queue: bot_messages
```

Depois basta executar o bot:

```sh
sudo docker-compose run --rm bot make run-console-broker
```

A segunda forma é utilizando o script `run-rocketchat` que é utilizado quando o bot é executado com o RocketChat como canal. Para isso, as mesmas variáveis devem ser configuradas no arquivo `docker/bot/bot.env`.
Lembre-se também de configurar como `True` a seguinte variável do serviço `bot` no arquivo `docker/bot-rocketchat.env`.

```
# Broker config
BROKER_URL=rabbitmq
BROKER_USERNAME=admin
BROKER_PASSWORD=admin
QUEUE_NAME=bot_messages
```

Ao final é necessário buildar novamente o container do bot.

```
sudo docker-compose up --build -d bot
```

### Setup ElasticSearch

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

### Setup Kibana (Visualização)
Para a análise dos dados das conversas com o usuário, utilize o kibana, e veja como os usuários estão interagindo com o bot, os principais assuntos, média de usuários e outras informações da análise de dados.

O Kibana nos auxilia com uma interface para criação de visualização para os dados armazenados nos índices do ElasticSearch.

```
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



## Testando Fluxos de Conversa

É possível testar os fluxos de conversação utilizando o [Evaluation do Rasa Core](https://github.com/lappis-unb/tais/wiki/Testes-Automatizados). Para testá-los no seu bot basta adicionar um arquivo dentro do diretório `bot/e2e/` com as histórias a serem testadas. Essas histórias devem ser descritas normalmente, porém com exemplos de frases para cada uma das *Intents* sendo testadas, segundo o formato abaixo:

```
## História de teste 1
* cumprimentar: oi
   - utter_cumprimentar
* action_test: test custom action
   - action_test
```

Uma vez que os arquivos de teste foram adicionados ao diretório correto, basta rodar os testes com a *task* do bot:

```sh
sudo docker-compose run --rm bot make test-stories
```

Para gerar data-science referente aos testes automatizados de bor, execute o seguinte comando do *Makefile* na raíz do projeto:

```sh
sudo docker-compose run --rm bot make test-dialogue
```

## Notebooks - Análise de dados

### Setup

Levante o container `notebooks`

```sh
docker-compose up -d notebooks
```

Acesse o notebook em `localhost:8888`



## Tutorial para levantar toda a stack

```sh
sudo docker-compose up -d rocketchat

sudo docker-compose up -d rabbitmq
sudo docker-compose up -d rabbitmq-consumer

sudo docker-compose up -d elasticsearch
sudo docker-compose run --rm -v $PWD/analytics:/analytics bot python /analytics/setup_elastic.py
sudo docker-compose up -d kibana

sudo docker-compose up -d bot
```


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
