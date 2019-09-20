# Criação de Testes Automatizados
 
Ao construir um bot com o framework Rasa, deve se ter em mente como funciona a construção do diálogo do ponto de vista do bot, como ele processa todas as informações que são jogadas. O bot agrega uma concepção de um ser que interage e que se mostra "pensante", mas os desenvolvedores devem ter noção de como um bot age, como ele constrói todas suas previsões de diálogo e as usa a seu favor.
 
Imagine que começamos a fazer um bot qualquer, com um escopo definido, ao construirmos todas as estruturas necessárias para que ele responda e entenda, na verdade estaremos construindo a sua rede neural, que na parte humana seria a associação que fazemos da resposta a uma pergunta. Dessa forma, a rede neural é baseada na inserção de conteúdo e a ligação do mesmo a interação com o usuário, por exemplo no Boiler-Plate, ao colocarmos cada vez mais assunto, estamos expandindo nosso escopo e deixando nosso bot mais "inteligente". Em suma, as redes neurais são construídas a partir do treinamento do bot, que possibilita-o prever respostas, sintetizando os fluxos possíveis mediante a intenção do usuário.
 
No Rasa isso é feito de uma forma muito simples, ao criarmos novas intents e stories, damos abertura ao nosso bot dialogar sobre mais assuntos. Infelizmente temos um grande problema nesse quesito, ao inserirmos mais conteúdo, estamos abrindo espaço para que nosso bot esteja confundindo algum fluxo com outro.
 
Para inserirmos mais conteúdo em nosso bot de forma segura, utilizamos os testes automatizados que identifica se o novo conteúdo foi interferido ou interferiu em outro fluxo, acarretando em uma validação de fluxo e trazendo uma evolução muito mais fácil em estrutura e conteúdo.
 
Para construirmos os testes devemos primeiro escolher um fluxo no qual queremos tratar, depois estruturar uma conversa para esse fluxo, que nos permite avaliar todo o escopo que escolhemos. Por exemplo, no BoilerPlate temos a intent esporte e queremos ter a certeza que ela sempre estará funcionando. Nesse contexto, podemos gerar um diálogo que condiz com o que queremos:
 
```
 Usuário
 
- oi                                  (intent cumprimentar)
- qual o seu jogo favorito?           (intent esporte)
- tchau                               (intent despedir)
```

Esse é um exemplo bem simples, que conseguimos tirar dele informações que confirma o fluxo que queremos e nos informa se alguma mudança ocorreu.
 
Para construirmos o código dos testes, primeiro devemos entender que ao criarmos o fluxo que queremos temos que identificar a utter que corresponde aquela intenção:

``` 
 Usuário                              Bot
 
- oi                            ->     utter_cumprimentar
- qual o seu jogo favorito?     ->     utter_esporte                   
- tchau                         ->     utter_despedir
```

Agora fazer o código fica bem mais fácil:

```
## end-to-end story 1
* cumprimentar: ola
  - utter_cumprimentar
* esporte: qual o seu jogo favorito?
  - utter_esporte
* despedir: tchau
  - utter_despedir
```

O código é um arquivo MarkDown composto por um título que indica que estamos trabalhando com arquivos de ponta a ponta, em seguida dizemos a intent e o texto pré estabelecido para o teste, embaixo dizemos a utter que corresponde ao texto.
 
Esse código está localizado no coach/data/e2e, nele concentramos todos os arquivos de teste, como boa prática é comum começarmos o nome do arquivo de "e2e".
 
## Executando os arquivos e2e
 
Todas as informações de como executar os arquivos de teste está descrito no README do [BoilerPlate](https://github.com/lappis-unb/rasa-ptbr-boilerplate)

## Entendendo os resultados

Sabe-se que o teste do Rasa nos possibilita avaliar o fluxo de ponta a ponta, com as intenções pré definidas pelo mesmo, desta forma, ele nos disponibiliza uma forma de visualização desse teste no qual ele nos fornece:

    "precision" - quantidade de utters_esperadas divididas pela quantidade de utters_ocorridas
    "recall" - porcentagem de respostas que corresponderam a utter esperada.
    "f1-score" - a porcentagem de relação da precisão com o recall, sendo (2x precisão x recall) / (precisão + recall)
    "support" - o tanto de vezes que teste utiliza cada variável.

Matriz:

Desses dados gera uma matriz pelo script que permite visualizar a distribuição de confiança para todas as previsões

Essa matriz nos permite visualizar a relação entre as utters_esperadas (criadas pelos testes) e as utters_ocorridas (as que realmente foram respondidas mediante ao fluxo), priorizando o fluxo em que a conversa segue e a intenções que as correspondem, como pode ser visto no exemplo acima onde todas as utters_esperadas correlacionam com as utters_ocorridas. Forma-se uma matriz quadrada onde sua coluna 0 e linha 0 são respectivamente, a quantidade de utters_esperadas que correlacionaram com as utters ocorridas + as utters_esperadas que não resultaram em nenhum valor e a action_list (o numero de intenções no teste).

Há apenas uma exceção nesse quesito, quando houver um texto que retorne o fallback, ele criará uma matriz onde a coluna 0 e linha 0 são respectivamente, fallback e NONE. Isso pode ser visto na imagem abaixo no qual o texto retornou um fallback e a relação com a utter_esperada na ultima linha.

Pode-se dizer que as linhas são a utters_esperadas e as colunas são as utters_ocorridas, e os números são as quantidades de vezes que uma utter corresponde a outra ou deixa de corresponder naquele fluxo da conversa. Quando as utters_esperadas são relacionadas com as corretas utters_ocorridas este número irá ficar na diagonal principal sinalizando a quantidade de vezes de correspondência.

Na matriz pode-se perceber que existem dois números fora da diagonal principal, eles correspondem a utters que não corresponderam a sua respectiva resposta esperada. No número fora da diagonal na linha 0, conclui-se que é uma ação que ocorreu de algum utter que não foi esperada, já no segundo número fora da diagonal é uma utter esperada que não correspondeu a utter_ocorrida.