# Configuração da Policy do chatbot


Este tutorial tem como objetivo mostrar como funciona a configuração do treinamento de um *chatbot* contruido em **_Rasa_**, mostrando como funciona as **Policies**, suas características, e os hiperparâmetros necessários para configurá-las.

As informações mais detalhadas sobre as policies podem ser encontradas na [documentação](https://rasa.com/docs/rasa/core/policies/) do Rasa, e a configuração usada como referência é a utilizada na [TAIS](https://github.com/lappis-unb/tais/blob/master/coach/policy_config.yml) 


## Policies

Na arquitetura do *Rasa* as policies são aquelas que recebem as intenções do usuários, já identificadas pelo *chatbot*, e a partir dessa informação determina qual ação será toma a seguir. Sem grande rigor, a **Policy**  recebe a entrada identificada como por exemplo `ìntent_cumprimentar` e preve qual será a resposta do *bot*, usando como base os exemplos de conversas.

O *Rasa* possue várias policies implementadas e também suporte para construção de policy customizada. As que serão detalhadas neste documento são as **Keras Policy**, **Memoization Policy**, **Embedding Policy** e **Fallback Policy**.

No arquivo `policies_config.yml`, ou `config.yml` é definido a sequência de prioridades das policies a ser executada. Normalmente, a **Memoization Policy** é a que tem maior prioridade, pois avalia se existe um storie nos arquivos de treinamento seguindo exatamente a conversa intepretada, e a **Fallback Policy** é última prioridade, e age se todas as outras não atingirem o nível de confiança adequado. Entre a **Memoization Policy** e a **Fallback Policy** normalmente é definido uma das policies detalhadas abaixo. Essas policies (**Keras Policy**, **Embedding Policy**) são redes neurais que inferem o contexto da conversa a partir de um histórico e prediz qual a ação mais adequada, com a sua respectiva probabilidade. Essas redes neurais são treinadas com os exemplos de conversas salvos na pasta "stories" dos dados.

### Keras Policy

Esta policy tem a rede neural implementada usando a biblioteca Python [Keras]https://keras.io). Formada por camadas utilizando o algoritmo **LSTM**.

Em sua configuração sugerida na documentação, ela vem acompanhada de duas **[Featurization](#featurization)**, __MaxHistoryTrackerFeaturizer__ e a __BinarySingleStateFeaturizer__

### Embedding Policy

Ou também, Recurrent Embedding Dialogue Policy ([REDP](https://arxiv.org/abs/1811.11707)), tem como foco tratar conversas não cooperativas do usuário com um desempenho maior que a Keras Policiy.

Tem-se como conversa não cooperativa:

    * Chitchat: "Small-talk" ou perguntas não relacionadas a tarefa
    * Correction: Correção de uma resposta anterior
    * Broad context: Perguntas referentes ao estado da tarefa (Ex: "Já te informei o local, tem como você me dar a informação agora?")
    * Narrow context: Perguntas relacionadas a contextos imediatos (Ex: quando o usuário pergunta o porquê da informação dada pelo bot)

Para fazer a previsão da ação do bot em uma conversa não comperetativa, essa policy tem o foco em ações tomadas anteriormente, não somente as antigas intents previstas.

Por padrão,o Rasa Core gera histórias mais longas, colando aleatoriamente a histórias pré-definidas. Pois quando ocorre stories assim:

```
# thanks
* thankyou
   - utter_youarewelcome

# bye
* goodbye
   - utter_goodbye
```
o objetivo é ignorar contextos anteriores e responder assim como descrito.

Porém, para o funcionamento da **REDP**, o contexto da intent é relevante, logo esse comportamento do Rasa deve ser evitado, assim `augmentation` é colocado `0`.

### Memoization Policy

A **Memoization Policy** é aquela que memoriza os dados de treinamento e prevê de acordo com as stories descritas. Se a próxima ação predita, dada a intent identificada for igual a um dado de treinamento, esta responderá com confiança de 1.0, caso contrário será 0.0. 

Nesta é importante a geração de bastante stories e também o uso de `augmentation` se as stories não dependerem de contexto.

### Fallback Policy

A policy Fallback é acionada quando nenhuma das outras policies atingem o nivel de confiança esperado. Assim que ela é chamada, esta executa a **Fallback Action** que é a resposta padrão do bot.

Nela, deve-se estabelecer o nível de confiança mímino que as policies devem atingir para que não execute o Fallback (**threshold**), tanto na parte do processamento de linguagem natural (NLU), que interpreta as intents do usuário, quando na parte da previsão (Core).


## Featurization

Existem dois tipos de Featurization para construir vetores que representem as conversas, a **State Featurizers** e **Tracker Featurizers**.

As **States Featurizers** utilizando o **tracker**, que dá informações de intents, entidades e slots prévios (ou seja, as **features**) e converte em um array.
  * Em BinarySingleStateFeaturizer, ele cria um vetor x,y que indica a presença de certas intent, entidades, ações anteriores e slots.
  * Na **LabelTokenizerSingleStateFeaturizer**, se cria uma vetor baseado nos nomes das features, separado em tokens e representados como **bag-of-words**. Por exemplo `utter_explain_details_hotel` e `utter_explain_details_restaurant` terão 3 features em comum.

Já as **Trackers Featurizers** itera pelos trackers states e chama o SingleStateFeaturizer para cada estado, sendo que a diferença entre os dois Trackers Featurizers são:
  * **FullDialogueTrackerFeaturizer**: cria uma representação numerica das stories para alimentar a rede neural.
  * **MaxHistoryTrackerFeaturizer**: cria um array dos estados anteriores para cada utter ou action do bot.


## Configuração

Algumas configurações utilizadas pela Tais, com base nas policies apresentadas. Lembrando que os valores de **threshold**, **augmentation**, **MaxHistoryTrackerFeaturizer** e entre outros, dependem do contexto que o bot trabalha e sempre é bom analisar a confiança e acurácia, para assim mudar os valores, se necessário.

Outra variável importante de se olhar para ver se todos os hiperparâmetros estão ajustados corretamente é o **loss**. Para sabe qual é o melhor número de épocas (*epoches*) o ideal é o maior valor de acurácia e menor valor de *loss*, indicando a maior precisão da rede neural e do seu bot. 

Só que deve-se levar em conta quão diferente esse valores ficaram, entre uma época e outra, pois se não acontecer uma redução significativa de loss e um aumento de acurácia, pode chegar ao *overfitting* da sua rede, e o bot ficar bom somente em casos específicos e não ser preciso em casos generalizados.

Resumindo, observe o loss e a acurácia, ajuste a época com um valor onde o loss é minimo e a acurácia é máxima, mas quando ainda ocorrer diferenças significativas entre uma época e outra.

### Keras + Memoization + Fallback

* Em **policies_config.yml**

```
policies:
  - name: KerasPolicy
    epochs: 7
    batch_size: 10
    featurizer:
      - name: FullDialogueTrackerFeaturizer
        state_featurizer:
          - name: LabelTokenizerSingleStateFeaturizer
  - name: FallbackPolicy
    nlu_threshold: 0.6
    core_threshold: 0.6
  - name: MemoizationPolicy
    max_history: 2

```

* Em **train.py**

```
'augmentation_factor': 20,
```

### Embedding + Memoization + Fallback


* Em **policies_config.yml**
```
policies:
  - name: "EmbeddingPolicy"
    epochs: 500
    attn_shift_range: 5
    featurizer:
      - name: FullDialogueTrackerFeaturizer
        state_featurizer:
          - name: LabelTokenizerSingleStateFeaturizer
  - name: FallbackPolicy
    nlu_threshold: 0.6
    core_threshold: 0.6
  - name: MemoizationPolicy
    max_history: 2
```
* Em **train.py**

```
'augmentation_factor': 20,
```
