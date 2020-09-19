# Rasa Boilerplate
<!-- badges -->
<a href="https://www.gnu.org/licenses/gpl-3.0.pt-br.html"><img src="https://img.shields.io/badge/licence-GPL3-green.svg"/></a>
<a href="https://codeclimate.com/github/lappis-unb/rasa-ptbr-boilerplate/maintainability"><img src="https://api.codeclimate.com/v1/badges/3fe22bf52000e147c6df/maintainability"/></a>
![badge_build](https://github.com/lappis-unb/rasa-ptbr-boilerplate/workflows/build_bot/badge.svg)


## For English version, see [README-en](docs/README-en.md)

## Tutorial para configurar todo o projeto

### Pré requisitos

Para rodar o projeto em sua máquina é necessário ter instalado:
- Docker
- Docker compose

### Primeiros passos

Primeiramente, clone o repositório para sua máquina local usando o comando:

```sh
git clone <Link para o repositório>
```

Para ter seu chatbot Rasa funcionando, certifique-se de estar dentro da pasta do projeto e então execute no terminal o seguinte comando:

```sh
make first-run
```

⚠️ **Atenção**: Caso ocorra algum erro de permissão, executar o comando `sudo make first-run`.


Esse comando irá construir a infraestrutura necessária (subir containers com as dependências, treinar o chatbot, etc) para possibilitar a interação com o chatbot.

Tudo está dockerizado então você não deve ter problemas de instalação do ambiente.

Depois que tudo for instalado, você verá a seguinte mensagem e pode começar a interagir com o bot

```sh
Bot loaded. Type a message and press enter (use '/stop' to exit):
Your input ->
```

Para fechar a interação com o bot é só dar `ctrl+c`.


Para conferir se os contêineres foram construídos corretamente, execute o comando:

```sh
docker ps
```
Se tudo der certo, você conseguirá ver uma tabela com dois contêineres de nomes `rasa-ptbr-boilerplate_bot-webchat` e 
`rasa-ptbr-boilerplate_actions` na coluna IMAGE.

Para iniciar uma conversa com o chatbot, execute o comando `make run-shell`, espere o comando rodar e divirta-se!


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

**Atenção**: o comando de treinamento é usado para criar os modelos necessários na conversação do bot. Para treinar o seu chatbot execute o comando:

```sh
make train
```

### Executando o bot no terminal
Para executar o bot no terminal execute:

```sh
make run-shell
```

### Executando o bot no Telegram

Após realizar o [tutorial](/docs/setup_telegram.md) de exportação de todas variávies de ambiente necessárias, é possível realizar a execução do bot no telegram corretamente.

**Antes de seguir adiante. Importante:** As variáveis de ambiente são necessárias para o correto funcionamento do bot, por isso não esqueça de exportá-las.

Edite o arquivo **credentials.yml** e descomente as linhas referentes ao telegram:

```sh
telegram:
 access_token: ${TELEGRAM_TOKEN}
 verify: ${TELEGRAM_BOT_USERNAME}
 webhook_url: ${TELEGRAM_WEBHOOK}
```

Depois execute o bot no telegram:

```sh
make run-telegram
```

### Analytics

Para a visualização dos dados da interação entre o usuário e o chatbot nós utilizamos uma parte da Stack do Elastic, composta pelo ElasticSearch e o Kibana. Com isso, utilizamos um broker para fazer a gerência de mensagens. Então conseguimos adicionar mensagens ao ElasticSearch independente do tipo de mensageiro que estamos utilizando.

* Para uma **configuração rápida** execute o seguinte comando:

```sh
make build-analytics
```

Espere até os serviço do *ElasticSearch* estar pronto, e execute o comando abaixo para configurar os índices:

```
make config-elastic
``` 

Espere até os serviço do *Kibana* estar pronto, e execute o comando abaixo para configurar os *dashboards*:

```
make config-kibana
``` 

O comando acima precisa ser executado apenas 1 vez e já vai deixar toda a infra de `analytics` pronta para o uso.

Acesse o **kibana** na url `locahost:5601`

Caso você deseje entender o processo de configuração da *stack* de *analytics*, veja a [explicação completa de analytics](docs/setup_analytics.md).

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
