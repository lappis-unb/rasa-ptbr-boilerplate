# Configuração pipeline de bot

O objetivo deste tutorial é explicar os passos necessários para configuração de um *pipeline* de *deploy* contínuo de um *bot* `Rasa`, utilizando o `GitLabCI`.

Os exemplos e estratégias utilizados neste tutorial são baseados no *pipeline* utilizado na TAIS. Para uma referência completa basta analisar o [arquivo de configuração](https://github.com/lappis-unb/tais/blob/master/.gitlab-ci.yml) do *pipeline* da TAIS no GitLab.

A configuração de *pipelines* utilizando o `GitLabCI` se dá a partir da utilização de um arquivo de configuração chamado `gitlab-ci.yml`. Neste tutorial aprenderemos  configurar um arquivo de utilização do *CI*.

Cada um dos *jobs* criados no *CI* são executados dentro de *containers* na infraestrutura do `GitLab`.

O primeiro passo para configuração é definir uma imagem base a ser utilizada nos *jobs* do *pipeline*. Pode-se definir uma imagem padrão que será utilizado em todos os *jobs* ou definir imagens diferentes para cada um dos *jobs* existentes.

Para definir uma imagem global é necessário utilizar a configuração abaixo:

```yml
image: python:3.6-slim

test style:
  stage: test style
  script:
    - pip -V
    - python -V
    - pip install -r dev.requirements.txt
    - flake8 --exclude venv

run dataset validator:
  stage: validate format
  image: lappis/coach:latest
  script:
    - cd coach/
    - make run-validator
```

No exemplo acima, foi definida uma imagem base chamada `python:3.6-slim`. Em seguida foram definidos dois *jobs* de teste, o primeiro deles utilizará a imagem padrão do python que foi definida na primeira linha, já que este não possui nenhuma *tag* de definição de imagem. O segundo *job* utilizará a imagem `lappis/coach:latest`, já que possui uma *tag* de definição de imagem que sobreescreve a imagem base.

## Definição dos stages

Os *jobs* serão criados a partir da organização em *stages*, sendo que estes serão executados de acordo com a ordem de prioridade definida. Essa característica define a dependência dos *jobs*, uma vez que caso o *job* de um estágio anterior falhe todos os *jobs* subsequentes de todos os próximos *jobs* serão cancelados e não serão executados.

Caso mais de um *job* seja definido com o mesmo estágio, a execução destes *jobs* será paralelizada pelo próprio `GitLab` e eles serão executados simultaneamente.

Uma estratégia que pode ser utilizada é separar os *jobs* do *pipeline* em três fases principais: *test*, *build* e *deploy*.

```yml
stages:
  - test
  - build
  - deploy
```

No *job* `test style` exemplificado acima, o *stage* é definido como `test`. Então ele será um dos *jobs* rodados no começo da execução do *pipeline*.

## Estratégia de Build

Como este tutorial é baseado na utilização de serviços `docker`, a estratégia de build é focada na construção e publicação da imagem utilizada pelos serviços.

Está exemplificado abaixo um *job* de build para imagens `docker` no CI do `GitLab`.

```yml
build bot:
  stage: build
  image: docker
  tags:
    - docker
  services:
    - docker:dind
  script:
    - docker login -u $DOCKERHUB_USER -p $DOCKERHUB_PASSWORD
    - docker build -f docker/bot/bot.Dockerfile -t lappis/bot:latest .
    - docker push lappis/bot:latest
  only:
    - master
  environment: homolog
```

A imagem utilizada deve ser a imagem `docker` e deve ser adicionada uma *label* que defina a utilização do serviço `docker:dind`, um acrônimo para "Docker in Docker". O que indica ao CI que serão utilizados comandos `Docker` dentro do *container* onde o *job* está sendo executado.

A *label* `script` define quais comandos serão executados durante esse *job*. Neste caso, são 3 comandos/etapas para a criação e publicação da imagem.

1 - Primeiro é feito o *login* no `Dockerhub` utilizando os dados de acesso configurados em variáveis secretas no próprio repositório. Para entender como utilizar estas variáveis no GitLab basta seguir a [documentação oficial](https://docs.gitlab.com/ee/ci/variables/);

2 - Logo após, a imagem é construída a partir do `Dockerfile` contido no próprio repositório do projeto, com o nome definido;

3 - Por último, a imagem é publicada e enviada para o *registry* do `Dockerhub`, e estará pronta para ser utilizada no estágio de *deploy*;

## Estratégias de Deploy

Serão ensinadas duas estratégias principais, estas estratégias são baseadas no uso de `docker` e arquiteturas de microserviços.
Existem diversas estratégias que podem ser adotadas para fazer o *deploy* de um serviço `docker`, aqui serão ensinadas duas delas: A primeira utilizando o protocolo `ssh` e a segunda utilizando uma aplicação chamada [Watchtower](https://github.com/containrrr/watchtower).

### Deploy via ssh

Para esta estratégia é utilizado um *job* que utiliza o protocolo `ssh` para criar uma sessão dentro da máquina onde será feito o *deploy* do serviço e atualizar o serviço `docker`.

O *job* definido a seguir executa um *script* `shell` chamado `deploy_bot` que faz autenticação na máquina através da senha do usuário `root` e o IP da máquina, estas informações estão configuradas utilizando as variáveis secretas do `GitLabCI`.

```yml
deploy bot to homolog:
  stage: deploy
  <<: *set_ssh_config
  environment: homolog
  script:
    - ./scripts/deploy_bot.sh $TAIS_SERVER_PASSWORD $TAIS_SERVER_IP
  only:
    - master
```

A linha `<<: *set_ssh_config` é uma referência à um conjunto de comandos que está definido no mesmo arquivo de configuração, sendo ele:

```yml
.set_ssh_config: &set_ssh_config
  before_script:
    - apt-get update -y
    - apt-get install sshpass -y
```

O que essa linha faz é executar os comandos acima no começo do *job*, instalando a dependência de `sshpass` utilizada no script `deploy_bot`. Como mostrado abaixo, esse *script* recria o serviço de *bot*, baixando a nova imagem e recriando o *container* para este serviço.

```sh
#!/bin/bash

sshpass  -p $1 ssh -o StrictHostKeyChecking=no root@$2 <<-'ENDSSH'
    cd rouana/
    docker-compose stop bot
		docker-compose rm -f bot
		docker-compose pull bot
    docker-compose up -d bot
ENDSSH
```

### Watchtower

O [Watchtower](https://github.com/containrrr/watchtower) é um serviço que monitora os *containers* criados dentro do mesmo contexto, e sempre que a imagem sendo utilizada pelo *container* é atualizada este serviço faz uma atualização no serviço, baixando a nova imagem e recriando o *container* do serviço com as mesma configurações, porém com a imagem nova.

Para utilizar esta estratégia basta adicionar um serviço utilizando a imagem do `watchtower` ao mesmo arquivo de configuração dos serviços, ou garantir manualmente que ele esteja na mesma rede dos serviços que se quer monitorar.
Além disso, é preciso adicionar uma label `com.centurylinklabs.watchtower.enable` indicando quais serviços devem ser ou não monitorados e atualizados de acordo com o valor que pode ser `false` ou  `true`.

```yml
version: '2'

services:

  kibana:
    image: docker.elastic.co/kibana/kibana:6.4.2
    restart: unless-stopped
    ports:
      - 5601:5601
    environment:
      - SERVER_PORT=5601
      - ELASTICSEARCH_URL=http://elasticsearch:9200
    depends_on:
      - elasticsearch
    labels:
      - "com.centurylinklabs.watchtower.enable=false"

  watchtower:
     image: containrrr/watchtower
     volumes:
       - /var/run/docker.sock:/var/run/docker.sock
     command: --interval 30
     labels:
       - "com.centurylinklabs.watchtower.enable=false"
```

O serviço `Watchtower` fica consultando o repositório da imagem a ser monitorado a cada X segundos, para saber ser houve alguma atulização ou não. O período de tempo utilizado nesta estratégi pode ser definido com o parâmetro `--interval`, como exemplificado acima onde é definido com o valor de 30 segundos.

Esta estratégia possui a vantagem de que a estratégia de *deploy* está totalmente contida dentro da própria infraestrutura onde estão rodando os serviços, desta forma não há dependência de um outro serviço e não é necessários ter credenciais de acesso configuradas em outros ambientes como na estratégia anterior. Além disso, caso o objetivo seja fazer somente *deploy* dos serviços e não haja um *pipeline* mais elaborado, utilizar esta abordagem traz uma solução simples para o problema. Porém, a utilização desta estratégia é menos flexível em relação à generização, uma vez que funciona apenas para estratégias de *deploy* baseadas em `docker`.

## Testando Jobs

Configurar corretamente um *pipeline* muitas vezes pode ser um processo um tanto quanto demorado e custoso, uma vez que o teste das configurações deve ser realizado diretamente no CI executando *builds* reais.

Para testar localmente alguns *jobs* e facilitar o processo de *debug* e configuração do *pipeline* é possível utilizar uma instância local do [GitLab Runner](https://docs.gitlab.com/runner/).

Utilizando como exemplo o *job* `test style`:

```yml
test style:
  stage: test style
  script:
    - pip -V
    - python -V
    - pip install -r dev.requirements.txt
    - flake8 --exclude venv
```

Para executar este *job* localmente bastaria [instalar o runner do GitLab](https://docs.gitlab.com/runner/install/),
e em seguida executar o seguinte comando:

```sh
gitlab-runner exec docker "test style"
```
