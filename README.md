# Rouana - Assistente Virtual da Cultura


## Ambiente RocketChat

```sh
sudo docker-compose up -d mongo
sudo docker-compose up -d mongo-init-replica
sudo docker-compose up -d rocketchat
```

Entre no rocketchat com o login `admin` e senha `admin`. Execute o script `bot_config.py` no
terminal

```sh
python3 scripts/bot_config.py
```

Vá no rocketchat e configure o webhook de saída, para isso vá em
`Administrations > Integrations > New Integration`, escolha `Outgoing WebHook`.
Preencha com as seguintes informações

```yaml
Event Trigger: Message Sent
Enabled: True
Channel: @rouana
URLs: http://rouana:5005/webhook
Post as: rouana
```

Depois clique em `Save Changes`

Por fim levante o docker da Rouana

```sh
sudo docker-compose up rouana
```

## Testes

### Teste de confiabilidade de frases

```sh
sudo docker run --rm --name rouana -it -v $PWD/rouana:/rouana rouana:console python confidence.py
```

### Conversa no console

```sh
sudo docker build -t rouana:console .
sudo docker run --rm --name rouana -it -v $PWD/rouana:/rouana rouana:console
```
