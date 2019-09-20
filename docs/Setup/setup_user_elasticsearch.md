### Configurando os usuários

Caso seja desejada a função de se ter usuários com diferentes permissões dentro do kibana, deve-se seguir os seguintes passos (Caso não seja esse seu interesse, pode passar para a próxima sessão):   

OBS: Os seguintes passos podem ser encontrados, com mais detalhes, na seguinte paǵina: https://www.elastic.co/guide/en/elastic-stack-overview/current/get-started-enable-security.html

**1. Habilitar função de segurança do elastic search:**

   Depois de se subir o container do elastic de acordo com a seção [Setup](https://github.com/lappis-unb/rasa-ptbr-boilerplate/tree/master#setup-elasticsearch),
   adicione a seguinte linha ao arquivo 'rasa-ptbr-boilerplate/elasticsearch/elasticsearch.yml':

```
xpack.security.enabled: true
```

Após adicionar a linha, reinicie o container do Elastic Search

```
sudo docker-compose restart elasticsearch
```


**2. Definir senhas para usuários internos do elasticsearch:**

 Entre no container com o comando:


```
sudo docker-compose exec elasticsearch bash
```

   Dentro do container execute o seguinte comando, preenchendo as senhas que deseja para cada um dos usuários.


```
./bin/elasticsearch-setup-passwords interactive
```

**3. Adicionar usuário kibana ao container do kibana**

   Depois de subir o container do kibana de acordo com a seção [Visualização](https://github.com/lappis-unb/rasa-ptbr-boilerplate/tree/master#setup-kibana-visualização), entre no mesmo com o comando:

```
sudo docker-compose exec kibana bash
```

   Dentro do container, execute os seguintes comandos, digitando, quando necessário, o usuário kibana, e a senha criada no passo anterior.

```
../bin/kibana-keystore create
../bin/kibana-keystore add elasticsearch.username
../bin/kibana-keystore add elasticsearch.password
```

Após executar os comandos acima, reinicie o container do kibana.

```
sudo docker-compose restart kibana
```


**4. Crie usuários além do administrador**

   Após os três passos anteriores, será possível entrar no kibana utilizando a conta com usuário 'elastic'.

   Na interface, é possível criar outros usuários, com diversas outras permissões, entrando em ***Management / Security / Users***, e após isso clicando no botão Create New User.

**5. Definir permissões para usuários.**

   Na criação de usuários é possível se definir permissões para cada um deles, utilizando os ***roles*** definidos pelo elastic.

   Por exemplo, um usuário que deva ter somente aceesso a leitura dos dashboards criados, deverá ter o role ***kibana_dashboard_only_user*** e ***apm_user***

   É possível criar novos ***roles*** em ***Management / Security / Roles***
