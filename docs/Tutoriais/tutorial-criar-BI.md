# Criação de visualizações no Kibana


## Escolhas tecnológicas

&emsp;&emsp; Para o monitoramento da interação **Usuário vs Chatbot** e do funcionamento do próprio bot, nós utilizamos uma parte da Stack do ElasticSearch, composta pelo próprio Elastic e também pelo Kibana.

* **ElasticSearch:** É uma _engine_ de busca em tempo real. O qual consiguimos aplicar diversos filtros e cachear as buscas já realizadas, tornando o acesso aos resultados já pesquisados muito mais rápido.  

 É importante ressaltar que o Elastic é baseado em documentos, então cada dado é um documento dentro do banco de dados.

* **Kibana:** O Kibana pertence a ElasticStack e nos fornece recursos de visualização em cima dos documentos armazenados no Elastic.

 Nos auxilia com gráficos pré-moldados, bastando relacionar com dados já existentes.

**Obs 1:** A escolha da utlização destas tecnologias condiz com a filosofia do laboratório, na qual acreditamos que devemos utilizar sempre que possível Software Livre. E estas tecnologias possuem planos que são SL e gratuitos.

## Criando visualizações

&emsp;&emsp; Com relação às visualizações, é necessário se ter em mente em qual contexto o seu chatbot está inserido e quais são as necessidades do seu cliente.

&emsp;&emsp; Neste tutorial iremos desenvolver algumas visualizações para métricas de negócio e de desenvolvimento que estão descritas no [estudo de métricas para bot](https://github.com/lappis-unb/tais/wiki/Estudo-sobre-metricas-para-bots). Teremos exemplos de:

* **Métricas de negócio**
  * Total de usuários;
  * Usuários por dia;


* **Métricas de desenvolvimento**
  * Perguntas não entendidas.

&emsp;&emsp; Para a criação das visualizações é necessário estar com o ambiente do Analytics configurado. Este ambiente é responsável por tornar possível a utilização dos serviços do ElasticSearch e  do Kibana. Você pode obter informações de como configurar no [README](https://github.com/lappis-unb/rasa-ptbr-boilerplate) do projeto.

&emsp;&emsp; Com o ambiente configurado e _up_, agora vamos entender um pouco mais sobre a interface do Kibana e como ela nos ajuda na criação das visualizações.

### Interface do Kibana

&emsp;&emsp; Após o serviço _up_, você encontrará essas informações na página inicial quando acessar o serviço do Kibana.

![image](https://user-images.githubusercontent.com/26297247/62138505-207b6980-b2be-11e9-9b91-982795187a74.png)

&emsp;&emsp; O nosso foco neste tutorial será nas opções **Discover**, **Visualize** e **Dashboard**. Nestas 3 funcionalidades nos conseguiremos abordar diversos recursos disponíveis para as visualizações.

* **Discover:** Nesta funcionalidade é possível a visualização em tempo real de todos os documentos em todos os índices que correspondem ao padrão do índice selecionado.  

  ![image](https://user-images.githubusercontent.com/26297247/62140231-ff684800-b2c0-11e9-9687-6415805c23d6.png)

  &emsp;&emsp;É possível identificar na barra lateral esquerda todos os atributos que foram definidos na criação do index do ElasticSearch, ou seja, cada documento pertencente ao banco possui todos esses atributos.

* **Visualize:** Este outro campo permite você criar diversas visualizações para os dados que estão armazenados nos índices do ElasticSearch.

  ![image](https://user-images.githubusercontent.com/26297247/62140819-ffb51300-b2c1-11e9-8184-031dc75e30c3.png)

* **Dashboards:** Essa opção é a funcionalidade aonde você pode criar uma ou mais interface que reunirá uma ou mais visualização criada nas opções anteriores (ou em outras funcionalidades, caso deseja usar).

  ![image](https://user-images.githubusercontent.com/26297247/62141900-b9f94a00-b2c3-11e9-9037-45b7acc80988.png)

  &emsp;&emsp; É importante cada dashboard ter sua própria finalidade. Por exemplo, se deseja ter visualizações para métricas de negócio e de desenvolvimento, seria interessante ter pelo menos um dashboard para cada tipo de métrica. Até porque os focos e o contexto são diferentes de cada um.

### Métricas

&emsp;&emsp; É importante ressaltar que sempre é necessário você entender em qual contexto você está inserido e pra qual público você está elaborando as visualizações, tendo em vista que há diversas maneiras de apresentar um dado.

&emsp;&emsp; Também é necessário tomar cuidado com algumas visualizações que podem se tornar tendênciosas com a maneira como ela é apresentada. Por exemplo gráficos de pizza, donuts, pie, entre outros do mesmo estilo. Nós humanos temos uma percepção menor de comparação de dados que estão apresentados em áreas, ainda mais circulares, que é o caso desses gráficos. Isso pode tornar sua visualização tendenciosa [1]. **Tome cuidado!**

&emsp;&emsp; Caso você não compreenda ou queira se aprofundar em algum conhecimento, cocê encontrará explicações mais profundas para cada termo como agregação, índice, filtro, etc, na documentação do [ElasticSearch](https://www.elastic.co/guide/index.html).

### Métricas de negócio

#### Total de Usuários

&emsp;&emsp; Optei por começar com a métrica **total de usuários** por ser um dado simples, composto somente por um único número. Não precisando de nenhum comparativo ou de uma outra dimensão.

&emsp;&emsp; Vamos começar na opção **Visualize** da barra lateral localizada na esquerda da página inicial do Kibana.

&emsp;&emsp; Após acessar a página você será redirecionado para uma área que mostrará todas as visualizações que você já criou (caso tenha criado alguma). Clique no **+** localizado no canto direito superior para criar uma nova visualização.

  ![image](https://user-images.githubusercontent.com/26297247/62154077-621b0d00-b2dc-11e9-81dc-f07af5054f5d.png)

&emsp;&emsp; Agora você terá que escolher qual tipo de visualização mais se adequa ao dado o qual deseja apresentar. Como dito anteriormente, a métrica Total de Usuários é um único número que não precisa de comparação com nenhum outro dado e também não precisa ser apresentado em duas dimensões, é um dado simples. Tendo isso em vista, a nossa escolha será então a opção **Metric (42)**, que é uma visualização de número simples.

  ![image](https://user-images.githubusercontent.com/26297247/62140819-ffb51300-b2c1-11e9-8184-031dc75e30c3.png)

&emsp;&emsp; Agora terá que escolher o índice, responsável por armazenar os dados no ElasticSearch, a sua escolha. No meu caso irei utilizar o **messages** que é o principal, e que estão todos os documentos que precisamos. Caso não tenha nenhum criado, você poderá criá-lo no **Menagement -> Index Pattern**.

  ![image](https://user-images.githubusercontent.com/26297247/62156245-fdae7c80-b2e0-11e9-82a1-fe3b9c7984ff.png)

&emsp;&emsp; Após escolher o índice você será redirecionado para a página de edição da visualização. O valor apresentado à direita/centro refere-se à contagem de todos os documentos presentes no índice escolhido, por isso, provavelmente, é um valor maior do que o esperado. Por causa do tipo da agregação que vem por padrão.

  ![image](https://user-images.githubusercontent.com/26297247/62156921-5df1ee00-b2e2-11e9-9698-94d3ecde6c23.png)

&emsp;&emsp; À esquerda da visualização temos umas opções de edição onde podemos escolher o tipo da agregação que queremos: **contador, média, máximo, mínimo, porcentagem, dentre outras**.

  ![image](https://user-images.githubusercontent.com/26297247/62156827-25eaab00-b2e2-11e9-9ee1-82d29234112f.png)

&emsp;&emsp; Os documentos são compostos por todos as interações dos usuários com o bot. Logo, um único usuário terá mais de um documento armazenado no índice, então temos que fazer uma contagem única por usuário na agregação, **Unique Count**.

&emsp;&emsp; Ao escolher a opção de **unique count** aparecerá abaixo do aggregation uma opção de **field**, nela estarão listados todos os atributos de um documento. Escolha então o campo de user_id e clique no botão de **Apply Changes**, seta na barra de opções, ou aperte CTRL+ENTER para as modificações serem aplicadas.

  ![image](https://user-images.githubusercontent.com/26297247/62157363-5bdc5f00-b2e3-11e9-85ef-1102c7da6f6e.png)

&emsp;&emsp; Após a aplicação das mudanças o Kibana já irá te retornar o valor da quantidade de usuários no período de tempo definido no canto superior direito (extremo total).

  ![image](https://user-images.githubusercontent.com/26297247/62157612-f5a40c00-b2e3-11e9-8b1f-4bd558d8280a.png)

&emsp;&emsp; Caso deseje mudar a legenda do dado, escreva o texto na opção de **Custom Label** da agregação.

  ![image](https://user-images.githubusercontent.com/26297247/62158063-0012d580-b2e5-11e9-9836-58c31d4d66e4.png)

&emsp;&emsp; Agora vamos salvar a visualização para posteriormente adicionarmos a um dashboard. Clique na opção **Save** na barra superior. Escolha um nome para a visualização e salve.

  ![image](https://user-images.githubusercontent.com/26297247/62157962-b9bd7680-b2e4-11e9-80d1-668eb030550b.png)

#### Usuários por dia

&emsp;&emsp; A criação da visualização anterior foi utilizada para introduzir alguns termos e algumas ações que podemos tomar dentro do Kibana, agora iremos um pouco mais rápido.

&emsp;&emsp; Continuaremos no **Visualize** e vamos escolher agora uma visualização que nos auxilie a apresentar corretamente o nosso dado. Então precisaremos mostrar em um eixo a quantidade de usuários e em outro eixo os dias. Poderíamos então utilizar o Line, Area, Vertical Bar, Horizontal Bar, entre outros.

&emsp;&emsp; No tutorial iremos usar o **Vertical Bar**, gráfico representado em duas dimensões e que possui uma análise mais fácil, tendo em vista que a comparação da quantidade de usuários pelos dias é feito somente pela visualização da dimensão do eixo Y, quanto maior, mais usuários possui.

&emsp;&emsp; Nas opções de configuração da visualização teremos em **Metrics** o nosso eixo Y e logo abaixo, em **Buckets**, o eixo X.

* **Eixo Y:** Representará a quantidade de usuários

* **Eixo X:** Representará o espaço de tempo (dia, semana, mês ...).

&emsp;&emsp; Então vamos aplicar o mesmo conhecimento da visualização anterior, Total de usuários. Na configuração do eixo Y iremos fazer um contador unico dos usuários, selecionando o campo do **user_id**.  

  ![image](https://user-images.githubusercontent.com/26297247/62159648-98f72000-b2e8-11e9-9bfa-992c3b901072.png)

&emsp;&emsp; No campo do **Buckets** iremos criar o nosso eixo X e escolher uma agregação para o gráfico que entenda o nosso campo de tempo (**timestamp**) e consiga aplicar determinados filtros para intervalo de tempo. A agregação mais adequada é o **Date Histogram**.

  ![image](https://user-images.githubusercontent.com/26297247/62159784-ebd0d780-b2e8-11e9-9121-7a561f509f69.png)

&emsp;&emsp; Você pode deixar o intervalo de tempo como **Auto** ou definir um intervalo fixo (semanalmente, diáriamente, etc). Escolheremos o **daily** e aplicaremos as mudanças.

  ![image](https://user-images.githubusercontent.com/26297247/62159976-52ee8c00-b2e9-11e9-8847-b6a1d8aee010.png)

&emsp;&emsp; Agora basta salvar como uma nova visualização e começar a brincar e fazer outras. =D

### Métricas de desenvolvimento

#### Perguntas não entendidas

&emsp;&emsp; Nesta etapa vamos aprender um pouco mais de como utilizar o **Discover**.

&emsp;&emsp; Essa métrica pode ser entendida como uma número bruto sobre a quantidade de perguntas não entendida, ou então, mostrar os textos das perguntas que realmente o bot não entendeu. Para fazer a primeira opção, os tutoriais anteriores dão uma boa base. Agora vamos implementar a segunda opção.

&emsp;&emsp; Quando acessamos o **Discover** caímos diretamente em uma página que nos lista todos os documentos e seus atributos separadamente.

  ![image](https://user-images.githubusercontent.com/26297247/62163352-8c76c580-b2f0-11e9-9201-41d9fee2ed97.png)

&emsp;&emsp; Por _default_, mesmo não estando adicionados, todos os atributos são listados na visualização. Porém, podemos escolher quais queremos separadamente. Basta passar o mouse em cima do campo desejado e clicar no botão de **ADD**. Aparecendo logo acima como **Selected fields**.

  ![image](https://user-images.githubusercontent.com/26297247/62163587-0b6bfe00-b2f1-11e9-95c6-893ebf7afa73.png)

&emsp;&emsp; Agora temos todos os documentos que possui o atributo is_fallback. Porém, como definido na configuração do índice do Elastic, todos os documentos, mesmo não sendo um _fallback_ tem o atributo. Então precisamos aplicar um filtro para que tenhamos somente as mensagens que o bot não compreendeu.

&emsp;&emsp; No campo esquerdo superior tem a opção de **Add filter +**, no qual nos permite aplicarmos uma query de filter na busca que estamos realizando, que no caso é saber qual é mensagem caiu no _fallback_ ou não.

  ![image](https://user-images.githubusercontent.com/26297247/62163868-acf34f80-b2f1-11e9-9c0c-0c4fca1c2e72.png)

&emsp;&emsp; Você mesmo pode programar uma query clicando na opção de **Edit query SDL**. Mas o Kibana já nos fornece uma funcionalidade que ele entende o tipo do atributo e fornece uma interface para aplicar condições e filtros. Então escolhemos o atributo que queremos, que é o que estamos realizando a busca **is_fallback**, falamos que queremos aplicar o filtro quando ele for **True**, ou seja, faremos uma busca somente nos documentos que possuem um campo **is_fallback = True**. Colocando a opção do meio como **is** e a última opção como **True**.

  ![image](https://user-images.githubusercontent.com/26297247/62164404-baf5a000-b2f2-11e9-9996-5e50c406df06.png)

&emsp;&emsp; Agora já estamos com o filtro aplicado, so que não temos o texto das mensagens, então precisamos adicionar mais um atributo aos campos selecionados. Escolhemos o campo **Text**, e XABLAU, apareceram todas as mensagens que caíram no Fallback.

  ![image](https://user-images.githubusercontent.com/26297247/62164544-fb551e00-b2f2-11e9-97d9-887d04307b44.png)


&emsp;&emsp; Salvamos como uma nova visualização para finalizar.

### Dashboards

&emsp;&emsp; Um dashboard exibe uma coleção de visualizações, pesquisas e mapas. Você pode organizá-lo a seu gosto.

### Como unir as informações em um único lugar

&emsp;&emsp; Criaremos então um Dashboard na funcionalidade de **Dashboard** localizada na barra da lateral esquerda principal.

  ![image](https://user-images.githubusercontent.com/26297247/62164836-833b2800-b2f3-11e9-8464-9093ec567e82.png)

&emsp;&emsp; Após criar, você será redirecionado para uma página que mostrará uma mensagem dizendo que o dashboard está vazio, então temos que adicionar as visualizações que criamos. Vamos clicar na opção **Add** da barra superior.

  ![image](https://user-images.githubusercontent.com/26297247/62164950-bed5f200-b2f3-11e9-9dd6-5c046a6ca196.png)

&emsp;&emsp; As visualizações que criamos no **Visualize** estão listadas na primeira aba, **Visualization** quando clicamos no **Add**. Ela já aparece por default como selecionada. Então escolha as visualizações que deseja, dentre as que estarão listadas. Repita isso para todas as visualizações que deseja adicionar.

  ![image](https://user-images.githubusercontent.com/26297247/62165163-39067680-b2f4-11e9-80a8-35d4fdf576eb.png)

&emsp;&emsp; Agora para adicionar a visualização que criamos no **Discover** você terá que clicar novamente no **Add**, só que ir na segunda aba, **Saved Search**. Lá estarão listadas as querys que já salvas ou então as visualizações do **Discover**. Selecione a que deseja e pronto.

  ![image](https://user-images.githubusercontent.com/26297247/62165354-9ef2fe00-b2f4-11e9-8c67-3539dfe1fabf.png)

&emsp;&emsp; Agora basta salvar o Dashboard e desfrutar dos dados!!!

### Extras

&emsp;&emsp; Você pode compartilhar os dashboards como iframes caso deseja. Opção disponível na barra superior dentro do dashboard.

&emsp;&emsp; Caso queira se aprofundar um pouco mais, temos um vídeo sobre **Métricas para bots** no nosso canal do youtube [Lappis-unb](https://www.youtube.com/channel/UCbZvFMRd5NaPiqj0w4uU8RQ/featured).

## Referências

[1] Storytelling com dados, um guia sobre visualização de dados para profissionais de negócios. Cole Nussbaumer Knaflic.

[-] [Métricas para bot](https://github.com/lappis-unb/tais/wiki/Estudo-sobre-metricas-para-bots).
