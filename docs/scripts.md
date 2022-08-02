## Scripts

### Descrição

O script serve para automatizar as configurações do projeto através dos endpoints disponibilizados pela rocketchat:
- [User Endpoints](https://developer.rocket.chat/reference/api/rest-api/endpoints/team-collaboration-endpoints/users-endpoints)
- [Livechat Endpoints](https://developer.rocket.chat/reference/api/rest-api/endpoints/omnichannel/livechat-endpoints)

Funcionalidades do **script**:
- [x] Configurar Bot
- [x] Configurar Livechat
- [x] Configurar Departamento

### Passo-passo

Valores **default**:<br> 
- *admin_name* : boss
- *admin_password* : boss
- *bot_name* : rasa_bot
- *bot_password* : rasa_bot

``` sh
python3 scripts/config_env.py
```

Argumentos aceitos:<br>
- *-an* : admin_name
- *-ap* : admin_password
- *-bn* : bot_name
- *-bp* : bot_password

Exemplo:
``` sh
python3 scripts/config_env.py -an boss -ap boss -bp rasa_bot -bp rasa_bot
```

### Pip

- json
- logging
- requests
- argparse
