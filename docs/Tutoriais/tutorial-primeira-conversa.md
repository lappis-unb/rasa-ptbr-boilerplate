# Primeira Conversa

O Boilerplate vem com a prosposta de facilitar a criação de um chat-bot para diferentes contextos, desenvolvendo uma estrutura um tanto complexa, mas com passos simples para seu bot conseguir dar os primeiros avanços do jeito que desejar.

As ferramentas utilizadas nessa tutorial foi estudada e utilizada pelo LAPPIS (Laboratório de produção, pesquisa e inovação em software), para criação da Tais, um chat-bot que visa explicar os conceitos e novidades sobre a lei de incentivo à cultura do Brasil. No cume do nosso projeto, foi utilizado o Rasa NLU, uma ferramenta open source para processamento de linguagem natural, sendo focada em classificação de intenções e extração de identidades, e o Rasa Core, uma ferramenta livre para construção de sistemas de conversação.

Na utilização dessas ferramentas, há a necessidade de ter um arquivo domain.yml que define o contexto em que o bot está inserido. Dentro desse arquivo são especificadas as intenções e ações a serem utilizadas durante a execução do bot.

A primeira coisa a se fazer é clonar o repositório do BoilerPlate localmente.

Dentro do diretório `coach/data` há uma pasta chamada `intents`, que contém vários arquivos mark-down, que definem os textos relacionados à cada intenção. E outra pasta chamada `stories`, que contém vários arquivos mark-down, que descrevem os contextos de conversação esperados a partir das intenções.

Então vamos fazer passo a passo de como criar o seu primeiro chatbot.

## Intent

Se imagine conversando com uma pessoa, vocês estão tentando decidir qual será os sabores de pizza que vocês irão comprar para jantar. A cada frase formulada pelos dois, deve-se observar que tem um intuito naquilo que é falado. Para construção de um bot, tiramos esse conceito e damos o nome de intents, dessa forma conseguimos estruturar muito bem o que o nosso bot irá dizer, definindo o assunto que corresponderá todo o escopo de conversação, ou seja, a partir do que o usuário interage, conseguimos esteriotipar a sua fala, dando uma intenção para aquilo.

As intents são criadas em um arquivo Mark-Down, onde ele se baseia na estrutura do arquivo para determinar qual tipo de exemplo de frase corresponde a intent. A estrutura para as construções de intents é bem simples, primeiramente precisamos especificar que é uma intent `#intent:`, ao colocar assim estamos dizendo que existe uma nova intent naquele arquivo (Você pode acompanhar acessando um dos arquivos na pasta coach/data/intents). Em frente, você colocará o nome da intent `#intent: nome_intent`, por exemplo:

``` MarkDown
#intent: sabores_pizza
```

Para a finalização das intents você precisa dar exemplos de assunto, ou seja, como no nosso exemplo da `intent: sabores_pizza`, temos vários exemplos no qual podemos identificar como sabores de pizza que o usuário poderá falar, como calabreza, mussarela, a moda, etc:

``` MarkDown
#intent: sabores_pizza
    - Quais sabores vocês tem?
    - Quais são os sabores?
    - Você pode me dizer os sabores
```

Assim você pode dar vários exemplos para que o bot seja treinado e consiga entender vários sabores de pizza :)

## Utter

Em um bot, devemos esperar que ele não consiga fazer a formulação das frases sozinho. Na construção do bot a partir do Boiler-Plaite, há um arquivo chamado domain, encontrado dentro da pasta `coach/`, onde a primeira vista fica muito dificil de se analisar e compreender o que está ocorrendo, mas que ficará tudo claro logo.

Domain é um arquivo yml, que é composto por uma estrutura bem simples:

Na primeira parte do domain podemos perceber que está sendo listado todos os nomes das `intents` que compõe o Boiler-Plaite, nessa parte estamos especificamos quais são os assuntos que o nosso bot consiguirá responder.

Em seguida há o nome `entities`, que é o conteúdo que agrega a corrente principal de fluxo de conversa do seu bot, sendo assim, podemos perceber a partir das entities do que nosso bot irá falar descartando o fluxo natural que imaginamos  que um bot deverá seguir (claro que esse fluxo pode ser mudado ao gosto do usufruidor).

Após entities temos `templates`, que é composto de todas as respostas que o bot pode fazer, damos o nome de utters. Na primeira parte podemos perceber, uma utter muito importante para a construção de qualquer bot, a `utter_default`, essa utter tem o objetivo de sinalizar ao usuário que não está entendendo o que ele está falando ou orienta-lo a falar de uma forma mais compreensivel para o bot. Para construirmos uma utter primeiramente devemos dar o nome como por exemplo `utter_sabores_pizza:`, por convenção colocamos a primeira palavra de utter. Após o nome iremos complementar com `- text: |`, sinalizando que iremos escrever um texto e em seguida escrever a mensagem desejada, exemplo:

``` MarkDown
utter_sabores_pizza:
    - text: |
        temos calabreza, mussarela, a moda e portuguesa
```

Ao final do arquivo temos as `actions`, que é composta de todas as utters que criamos nos templates.

## Stories

Há várias coisas para se analisar em uma conversa, mas há uma coisa muito essencial em qualquer interação verbal: o assunto, ou um tema que corresponde aquele diálogo. Quando extraímos isso para âmbito do chat-bot, conseguimos denomina-los como stories, são eles que descrevem os contextos de conversação esperados a partir das intenções.

Na construção de um novo storie, você deve ir ao diretório `coach/data/stories` e acessar ou criar um arquivo mark-down com o nome relacionado a storie que será criada. Dentro do arquivo, primeiro você dá o nome do storie precedido de "##" e depois você lista em ordem o fluxo que a pessoa irá seguir, onde primeiramente você diz qual intent com "*" e depois a utter com "-", e é dessa forma que conseguimos correlacionar intents com utters, fazendo nosso bot entender e responder o esperado, exemplo:

``` MarkDown
## Oi Tudo Bem Story 1
    * cumprimentar
        - utter_cumprimentar
    * tudo_bem
        - utter_tudo_bem
```


## Executando e testando seu bot

Todas as informações de como executar e treinar seu bot está descrito no README do BoilerPlate. Para desenvolvimento sugerimos a utilização do console, já que o mesmo especifica o comportamento do seu chat-bot. Entrentanto se o desejado for a utilização de alguma plataforma de interação com o usuário, incentivamos a seguir o tutorial do RocketChat ou Telegram (https://github.com/lappis-unb/rasa-ptbr-boilerplate).

## Próximos passos


