## Contribuir com a Documentação

A documentação do projeto utiliza a ferramenta GitBook, e para contribuir com melhorias ou correções primeiro é preciso rodar localmente como mostra no [README](../../README.md).

Caso tenha alguma dúvida ou queira entender mais a fundo a ferramenta, acesse sua [documentação aqui](https://docs.gitbook.com/).


**Estrutura**: São necessários dois arquivos para que o gitbook funcione corretamente. O arquivo *readme* é primeira página da documentação e deve estar na pasta raíz como `./README.md`.
E o arquivo *summary* é o índice da documentação e deve estar também na pasta raíz como `./SUMMARY.md`. 


O gitbook cria htmls de todos os arquivos markdowns que estejam no `SUMMARY.md`.
 
### Primeiros passos

Então o primeiro passo para contribuir com a documentação é identificar se será uma correção, criação de conteúdo, organização e/ou atualização. 
Verifique se já existe uma [issue](https://github.com/lappis-unb/rasa-ptbr-boilerplate/issues) aberta sobre o assunto específico. Caso não tenha, [crie uma issue](https://github.com/lappis-unb/rasa-ptbr-boilerplate/issues/new/choose) e coloque a label de `documentação` e outra caso seja necessário. 
Rode localmente o gitbook para ver a documentação do projeto. 

1. Caso a contribuição não precise de criação de novos arquivos, faça as correções nos arquivos e abra um PR descrevendo claramente tudo o que foi feito.

2. Caso a contribuição envolva exclusão de arquivos, é muito importante verificar o arquivo `summary` e corrigir ou apagar os links que levariam para esses arquivos excluidos. Pois se não tirar desses arquivos, quando abrir vai dar erro.

3. Se a contribuição envolver atualização de nome de arquivos, é muito importante a correção também do arquivos `summary` e todos os outros que indiquem o redirecionamento, assim como testar antes de abrir o PR.

4. Se a contribuição envolver criação de novos arquivos, tente seguir o padrão, por exemplo, os tutoriais começam com `tutorial-nome-do-tutorial.md`. Após a criação de um novo arquivo é preciso colocar no arquivo `summary`, onde está o arquivo no projeto. Veja o exemplo do arquivo `./SUMMARY.md`.


O arquivo `./SUMMARY.md` segue a seguinte estrutura:


```markdown
‌# Summary​

## Use títulos para criar grupos de páginas

* [Introdução](README.md)
* [Setup]()    
    * [Setup Telegram](docs/Setup/setup-telegram.md)    
    * [Setup Slack](docs/Setup/slack.md)
    
* [Tutorial]()    
    * [Criar uma intent](docs/Tutoriais/tutorial-criar-intent.md)    
    * [Como usar slot](docs/Tutoriais/tutorial-usar-slot.md)    
    
## Segundo grupo de páginas

* [Introduction](docs/README-en.md)
```

Após alterações, rode novamente, verifique o `summary` e teste todos os links.


### Referências

[1] - [https://docs.gitbook.com/integrations/github/content-configuration#structure](https://docs.gitbook.com/integrations/github/content-configuration#structure)
