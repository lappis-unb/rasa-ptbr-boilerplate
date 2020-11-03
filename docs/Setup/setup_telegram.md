# Setup do bot no Telegram

Para configurar e ter seu bot no telegram, você precisa seguir os seguintes passos:
1. [Criar um bot no telegram com BotFather](#criar-um-bot-no-telegram-com-botfather)
1. [Executar o ngrok](#executar-o-ngrok)
1. [Exportar as variáveis](#exportar-as-variáveis)
1. [Atualizar o arquivo de credenciais](#atualizar-o-arquivo-de-credenciais)

## Criar um bot no telegram com BotFather

Converse com o [@BotFather do Telegram](https://t.me/BotFather) e crie um bot pra você seguindo as instruções dele.
Você vai sair de lá com duas informações importantes: o `token` e o `username` do seu bot.
Segura elas aí, pois vamos precisar em breve.


## Executar o ngrok

Precisamos configurar um webhook para fazer a comunicação do nosso bot com o telegram.
Para isso, vamos utilizar o [ngrok](https://ngrok.com/download).
Nesse link, você vai fazer o download. E executar o comando de unzip do arquivo.

Faça o download, extraia o arquivo que foi baixado e execute o comando a seguir.

```sh
./ngrok http 5001
```
Esse comando vai executar o ngrok na porta 5001. Ele vai ocupar o terminal em que for executado.

**Atenção:** O conector do Telegram está utilizando a porta 5001 como padrão.
Caso queira mudar, somente altere a porta utilizada pelo no Makefile.


## Exportar as variáveis

### Telegram

Após escolher um nome para seu bot, o @BotFather lhe dará um token para utilizar para acessar a API do Telegram.
Adicione ambos no [arquivo de configurações do bot], como a seguir.
Substitua o `TELEGRAM_TOKEN` pelo token lhe enviado pelo BotFather e `TELEGRAM_BOT_USERNAME` pelo nome do seu bot.

```sh
TELEGRAM_BOT_USERNAME=username_do_bot
TELEGRAM_TOKEN=token_fornecido_pelo_BotFather
```

### NGROK

Enquanto o ngrok estiver em execução, ele apresentará uma série de informações da sessão atual.
Copie a url do campo Forwarding com o protocolo `HTTPS` e cole no [arquivo de configurações do bot].
Substitua apenas o `your_webhook_server`. Mantenha o restante da linha

```sh
TELEGRAM_WEBHOOK=your_webhook_server/webhooks/telegram/webhook
```
> Lembre-se: sempre que executar o ngrok essa url deve ser atualizada.


Ao final de realizar essas configurações, seu [arquivo de configurações do bot] deve estar de acordo com o exibido logo abaixo:

```sh
TELEGRAM_BOT_USERNAME=<nome-do-seu-bot>
TELEGRAM_TOKEN=<token-do-seu-bot>
TELEGRAM_WEBHOOK=<link-do-seu-webserver-ngrok>/webhooks/telegram/webhook
```

## Atualizar o arquivo de credenciais

Edite o arquivo credentials.yml e descomente as linhas referentes ao telegram:
```
telegram:
 access_token: ${TELEGRAM_TOKEN}
 verify: ${TELEGRAM_BOT_USERNAME}
 webhook_url: ${TELEGRAM_WEBHOOK}
```
Não precisa trocar nenhuma informação, apenas descomentar essa seção do arquivo.


Com isso, é possível realizar a execução do bot com o comando

```
make run-telegram
```

Assim que rodar o comando, você pode conversar com o seu bot no telegram.
Basta procurar ele pelo username que você criou.

Para mais comandos e informações, veja o [README](https://github.com/lappis-unb/rasa-ptbr-boilerplate/blob/main/README.md)

[arquivo de configurações do bot]: https://github.com/lappis-unb/rasa-ptbr-boilerplate/blob/main/env/bot-telegram.env
