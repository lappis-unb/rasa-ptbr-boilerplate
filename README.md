# Tais - Assistente Virtual da Cultura


## Ambiente RocketChat

```sh
sudo docker-compose up -d rocketchat
```

Entre no rocketchat com o login `admin` e senha `admin`. Execute os comandos
a seguir para configurar e rodar a rouana

```sh
python3 scripts/bot_config.py
sudo docker-compose up rouana
```

Para que a assistente virtual inicie a conversa você deve criar um `trigger`.
Para isso, entre no rocketchat como `admin`, e vá no painel do Livechat na
seção de Triggers, clique em `New Trigger`. Preencha o Trigger da seguinte forma:

```yaml
Enabled: Yes
Name: Start Talk
Description: Start Talk
Condition: Visitor page URL
    Value: http://localhost:8080/
Action: Send Message
 Value: Impersonate next agent from queue
 Value: Oi eu sou a Taís, assistente virtual do MinC, e estou aqui para te ajudar a esclarecer dúvidas sobre a Lei Rouanet. Tudo bom?
```

O valor `http://localhost:8080/` deve ser a URL de acesso da Taís.


## Testes

### Conversa no console

```sh
sudo docker build -t rouana -f docker/Dockerfile .
sudo docker run --rm --name rouana -it -v $PWD/rouana:/rouana rouana python train.py
```

### Teste de confiabilidade de frases

```sh
sudo docker run --rm --name rouana -it -v $PWD/rouana:/rouana rouana python confidence.py
```

