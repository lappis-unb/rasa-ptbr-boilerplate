## Setup do bot no Telegram

##### Crie um bot no Telegram

Converse com o [@BotFather do Telegram](https://t.me/BotFather) e crie um bot de teste unicamente seu seguindo as instruções dele.




##### Exporte as variáveis do seu bot
Após escolher um nome para seu bot, o @BotFather lhe dará um token para utilizar para acessar a API do Telegram. Adicione ambos no [arquivo de configurações do bot](../docker/bot-telegram.env), como a seguir. Substitua o TELEGRAM_TOKEN pelo token lhe enviado pelo @BotFather e TELEGRAM_BOT_USERNAME pelo nome do seu bot.

```sh
TELEGRAM_BOT_USERNAME=token_fornecido_pelo_BotFather
TELEGRAM_TOKEN=username_do_bot
```

##### Execute o ngrok
Após a etapa anterior, é necessário utilizar o [ngrok](https://ngrok.com/download) para expor determinada porta para ser utilizado
pelo Telegram.

Conforme a seguir, execute o ngrok na porta 5001.

```sh
./ngrok http 5001
```

**Atenção:** O conector do Telegram está utilizando a porta 5001 como padrão. Caso queira mudar, somente altere
a porta utilizada pelo no Makefile.


##### Exporte a URL do Webhook 

Enquanto o ngrok estiver em execução, ele apresentará uma série de informações da sessão atual. Copie a url do campo Forwarding com o protocolo HTTPS e cole no [arquivo de configurações do bot](../docker/bot-telegram.env). ela será similar à seguinte.

```sh
TELEGRAM_WEBHOOK=link_do_ngrok/webhooks/telegram/webhook
```

::Lembre-se::: sempre que executar o ngrok essa url deve ser exportada.


##### Execução do bot no telegram

Ao final de realizar essas configurações, seu [arquivo de configurações do bot](../docker/bot-telegram.env) deve estar de acordo com o exibido logo abaixo:

```sh
TELEGRAM_BOT_USERNAME=lappisbot
TELEGRAM_TOKEN=token
TELEGRAM_WEBHOOK=your_webhook_server/webhooks/telegram/webhook
```

Com isso, é possível realizar a execução do bot seguindo os passos do [README](../README.md)

