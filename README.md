# Rasa Boilerplate

Um projeto feito em Rasa com configurações necessárias para a construção
de um projeto grande de chatbot.

Este projeto teve como base a [Tais](http://github.com/lappis-unb/tais).

## Bot

### RocketChat

```sh
sudo docker-compose up -d rocketchat
# aguarde 3 minutos para o rocketchat terminar de levantar
sudo docker-compose up bot
```

Para que a assistente virtual inicie a conversa você deve criar um `trigger`.
Para isso, entre no rocketchat como `admin`, e vá no painel do Livechat na
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

O valor `http://localhost:8080/` deve ser a URL de acesso do Bot.

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

**Atenção**: Você precisa alterar a variavel `host` dentro do código acima para a url do site onde estará
o seu Rocket.Chat.

### Telegram

Para realizar este processo, recomenda-se a criação de um [Bot para o Telegram](https://core.telegram.org/bots#3-how-do-i-create-a-bot) para obter todas as informações necessárias.

Para rodar a _stack_ do bot pelo Telegram juntamente com os serviços anexados, é necessário comentar a parte relacionada ao Rocket.Chat e descomentar o serviço relacionado ao bot do telegram.

Após, é necessário utilizar o [ngrok](https://ngrok.com/download) para expor determinada porta para ser utilizado pelo Telegram.

Ao baixar, é só executar utilizando o seguinte comando:

```
./ngrok http {porta utilizada}
```

**Atenção:** O conector do Telegram está utilizando a porta 5001 como padrão. Caso queira mudar, somente altere a porta utilizada pelo no Makefile.

Ao executar, será gerado um link onde será usado para recuperar todas as informações obtidas pelo webhook do Bot pelo Telegram, semelhante a este link:

```
Exemplo:
https://283e291f.ngrok.io
```

Configure todas as informações necessárias no docker-compose para integrar o bot do telegram criado:

```yml
- TELEGRAM_ACCESS_TOKEN={token fornecido pelo BotFather}
- VERIFY={username do bot}
- WEBHOOK_URL={link do ngrok}/webhooks/telegram/webhook
```

Para executar somente o serviço do bot para o Telegram, utilize o seguinte comando:

Se ainda não tiver treinado seu bot execute antes:

```sh
sudo docker-compose run --rm bot make train
```

Depois execute o bot no telegram:

```sh
sudo docker-compose up telegram_bot
```

### Console

```sh
sudo docker-compose run --rm bot make train
sudo docker-compose run --rm bot make run-console
```

### Train Online

```
sudo docker-compose run --rm bot make train
sudo docker-compose run --rm bot make train-online
```

## Analytics

### Setup

```
sudo docker-compose run --rm -v $PWD/analytics:/analytics bot python /analytics/setup_elastic.py
sudo docker-compose up -d elasticsearch
```

Lembre-se de setar as seguintes variaveis de ambiente no `docker-compose`.

```
ENVIRONMENT_NAME=localhost
BOT_VERSION=last-commit-hash
```

### Visualização

```
sudo docker-compose up -d kibana
```

Você pode acessar o kibana no `locahost:5601`




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

sudo docker-compose up -d kibana
sudo docker-compose run --rm -v $PWD/analytics:/analytics bot python /analytics/setup_elastic.py

sudo docker-compose up -d bot
```
