Este é um documento para orientação em como contribuir para o repositório do Rasa PT-BR Boilerplate. Antes de começar a contribuir veja as [issues já abertas](http://github.com/lappis-unb/rasa-ptbr-boilerplate/issues), e principalmente o funcionamento de nossa [arquitetura](https://github.com/lappis-unb/rasa-ptbr-boilerplate/blob/master/README.md).

Veja as orientações abaixo para cada tipo de contribuição:
* [Por onde começar a contribuir?](#comece-a-contribuir)
* [Reportar erros](#encontrou-um-bug)
* [Consertar erros](#concertou-um-bug)
* [Contribuir para a documentação](#quer-contribuir-para-a-nossa-documentação)
* [Adicionar nova feature](#quer-adicionar-uma-feature-nova-ou-ajudar-com-uma-existente)
* [Contribuir para o conteúdo do Boilerplate](#quer-contribuir-para-o-conteúdo-do-boilerplate)

### Comece a contribuir
Quer começar a contribuir para o Boilerplate? O processo em geral é bem simples:

- Crie uma issue descrevendo uma feature  que você queira trabalhar ou entre em issues já abertas (caso comece por uma issue já existente comente na issue que você está desenvolvendo).
- Escreva seu código, testes e documentação
- Abra um pull request descrevendo as suas alterações propostas
- Seu pull request será revisado por um dos mantenedores, que pode levantar questões para você sobre eventuais mudanças necessárias ou questões.

Veja nossa [documentação](https://github.com/lappis-unb/rasa-ptbr-boilerplate/tree/master/docs) para entender um pouco melhor sobre nosso código e [arquitetura](https://github.com/lappis-unb/rasa-ptbr-boilerplate/blob/master/README.md), veja nossas issues, principalmente as com as tags `help-wanted` e `good-first-issue`, que são as ideais para começar a contribuir para o Boilerplate.


### Encontrou um Bug?
Caso tenha encontrado algum erro, nos informe por uma issue, assim poderemos estar sempre melhorando. Pedimos que seja descritivo, dessa forma poderemos identificar e reproduzir o erro para ser possível consertá-lo.

Antes de reportar o Bug, veja as [issues com a tag `bug`](https://github.com/lappis-unb/rasa-ptbr-boilerplate/labels/bug) e verifique se o erro identificado já não possui uma issue criada.

Para uma boa documentação:
* Nomeie a issue com um nome claro e descritivo de acordo com o problema;
* Descreva o passo a passo para chegar no erro encontrado;
* Mostre exemplos do erro ocorrido;
* Descreva o comportamento esperado e o comportamento obtido;
* Marque a issue criada com a tag `bug`.

Veja a seguinte estrutura de issue:

``` markdown

**Descrição do erro encontrado:**
...

**Passo a passo para a reprodução do erro:**
1.
2.
...
**Comportamento esperado:** ...
**Comportamento obtido:** ...
```

### Consertou um Bug?
Para enviar a sua solução e consertar um bug existente, fork nosso repositório e crie um Pull Request descrevendo o problema e como ele foi corrigido.

Para uma bom Pull Request:
* Nomeie o PR de forma descritiva e clara de acordo com o problema resolvido;
* Descreva o problema e a sua solução;
* Marque a issue que o PR soluciona.

Veja o exemplo abaixo:

``` markdown
**Issue:** #[Número-da-Issue]
**Descrição do Problema:**
...
**Descrição da Solução:**
...
```

### Quer contribuir para a nossa Documentação?
Para contribuir com a documentação, veja a documentação já existente, e as issues pendentes para documentação marcadas com a [tag `documentação`](https://github.com/lappis-unb/rasa-ptbr-boilerplate/labels/documentação).

Caso queira resolver uma issue já existente, comente na issue que está trabalhando, caso ainda não exista uma issue crie uma nova issue descrevendo o problema encontrado e marque com a tag `documentação`.

Para solucionar faça um PR com a descrição do que foi feito e a referência a issue que está resolvendo.

### Quer adicionar uma feature nova ou ajudar com uma existente?

Nosso desenvolvimento é dividido em algumas frentes principais, sendo elas:
* **Bot Rasa:** Frente para o desenvolvimento do conteúdo do Boilerplate, com a utilização do Rasa (na pasta `bot`);
* **ElasticSearch:** Frente para o desenvolvimento de dashboards com Kibana para a análise das conversas do bot com os usuários (na pasta `analytics`);
* **Plataforma de Conteúdo:** Desenvolvimento de uma plataforma para adicionar conteúdo no Boilerplate, sem a necessidade de mexer diretamente nos arquivos do código ([no repositório `rasa-nlu-trainer`](https://github.com/lappis-unb/rasa-nlu-trainer)).

Além de que também temos algumas outras áreas, onde é possível contribuir, como:
* **Notebooks:** Notebooks jupyter para análise da estrutura e funcionamento do Bot (na pasta `notebooks`);

Aceitamos contribuições em todas as áreas do nosso código, desde que seja uma contribuição válida e traga reais melhorias para o projeto. Para fazer uma contribuição abra uma issue, com nome descritivo, especificando o que será feito e qual frente será afetada. Veja o exemplo abaixo de um bom template a ser feito:

``` markdown
**Frente a ser trabalhada:** ...
**Descrição da nova feature:**
...
**Porque essa feature melhoraria o código:**
...
```
Caso sua contribuição entre um uma das frentes principais, marque com a sua label específica. Temos as labels:
* `elasticSearch`: para issues da frente de análise do Elasticsearch com Kibana;
* `plataforma-conteudo`: para issues da frente do front-end de adicionar conteúdo no Boilerplate;
* `rasa`: Para issues sobre o Rasa, na frente do Bot.

Após fazer a issue, dê um fork do repositório e faça um Pull Request com sua nova feature. Dê um bom nome para o PR, especifique a sua solução, em qual frente ela se encaixa e a referência aissue relacionada. Veja o exemplo de uma estrutura de PR abaixo:

``` markdown
**Frente a ser trabalhada:**...
**Issue:** #[Número-da-Issue]

**Descrição da nova feature:**
...
**Descrição de como foi feito:**

**Descrição de como ela funciona:**
...
```

### Quer Contribuir para o conteúdo do Boilerplate?
Além de contribuição de código, o Boilerplate também possui contribuições de conteúdo. Veja as [issues marcadas com a tag `conteudo`](https://github.com/lappis-unb/rasa-ptbr-boilerplate/labels/conteudo). Comente na issue que está trabalhando, faça o fork e submeta seu PR. Lembre-se de  definir o que foi feito, linkar com a issue e marcar com a tag `conteudo`. Veja abaixo um exemplo de PR para contribuição de conteúdo.

``` markdown
**Issue:**#[Número-da-Issue]
**Conteúdo adicionado:**
* Exemplo de pergunta do usuário: ...
* Resposta: ...
...

```
