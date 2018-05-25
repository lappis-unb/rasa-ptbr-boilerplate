# Rouana

A Rouana é a assistente virtual de incentivo à Cultura em desenvolvimento pelo
MinC, em parceria com o LAPPIS (UnB - FGA), para interagir com os cidadãos
(produtores culturais e outros interessados) de forma simplificada com objetivo
de apoiá-los no entendimento da Lei Rouanet e no uso da plataforma SALIC.
O projeto é desenvolvido com tecnologias de chatbot como o Rocket Chat, e as
ferramentas Rasa NLU e Rasa Core.

## Ambiente de Desenvolvimento (com o RocketChat)

Dependências:
- [Docker](https://docs.docker.com/install/)
- [docker-compose](https://docs.docker.com/compose/install/)

Inicie o rocketchat com os seguites comandos:

```sh
docker-compose up -d mongo
docker-compose up -d mongo-init-replica
docker-compose up -d rocketchat
```

Acesse http://localhost:3000/ para entrar no RocketChat e continuar o resto da configuração do ambiente.

Crie o usuário `admin` com a senha `admin`. Então rode o script de configuração automática do ambiente:

```sh
python3 scripts/bot_config.py -an admin -ap admin -bn rouana -bp rouana -r http://localhost:3000
```

### Configurando o WebHook

É necessário configurar um WebHook de saída para redirecionar as mensagens do
chat para o servidor do Rasa Core. Para isso, vá em **Administração > Integrações > Nova integração > WebHook de Saída**.
Dentro da configuração do WebHook defina os campos da seguinte forma:

```
Event Trigger: Message Sent
Enabled: True
Channel: @rouana
URLs: http://rouana:5005/webhook
Post as: rouana
```

*Salve* as mudanças após a criação.

### Rodando o Bot

Para executar o bot é preciso configurar o arquivo `credentials.yml` com os dados correspondentes.
Depois disso, execute o container do bot:

```sh
docker-compose up rouana
```

