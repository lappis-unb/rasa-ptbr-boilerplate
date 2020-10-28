# Criação de Actions

A cada mensagem do usuário, o bot deve ser capaz de realizar uma atividade. Enviar uma mensagem de texto, chamar uma API, exibir uma imagem, salvar algum dado recebido, entre outras várias possibilidades. Para poder executar essas ações, o Boilerplate utiliza as Actions.  
Actions são arquivos py onde devem existir dois métodos fundamentais: ```name``` e ```run```.
- ```name```:
O método ```name``` recebe o parâmetro ```self``` e retorna uma string com o nome da action, que é a maneira como ela será chamada em outros arquivos do Boilerplate.  
- ```run```:
O método ```run``` também recebe o parâmetro ```self``` e mais outros três: o ```dispatcher```, que é responsável por retornar mensagens ao usuário, o arquivo ```domain``` e o ```tracker```, que é responsável por acessar a memória do bot, e ele retorna uma lista de eventos e respostas. É através desse método que as ações da action são realizadas.   

## Para criar uma action, siga os passos:
1) Crie um arquivo .py para a sua action em ```bot/actions```
2) Importe as seguintes bibliotecas:
```Python
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
```
3) Implemente os métodos ```name``` e ```run```

Exemplo de um método ```name```:
``` Python
    def name(self) -> Text:
        return "action_exemplo"
```
Exemplo de um método ```run```:
``` Python
 def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        try:
            dispatcher.utter_message("Eu sou uma action de exemplo")
        except ValueError:
            dispatcher.utter_message(ValueError)
        return []
```
4) Adicione o nome da sua action (o mesmo do retorno do ```name```) na parte de ```actions``` do arquivo ```domain```, na pasta ```bot```
```yml
actions:
- action_exemplo
```
5) Por fim, crie um storie para a sua action no arquivo ```stories``` em ```bot/data```, utilizando novamente o nome dado para a sua action
``` MarkDown
## story_da_action
* intent_da_action
    - action_exemplo
```
## Executando e testando sua action
As informações de como executar e treinar seu bot estão descritas no README do BoilerPlate. Entretanto, sempre que criar ou modificar uma action, lembre-se de parar o contêiner de actions, para que este possa subir novamente com as modificações feitas.  
### Parando um contêiner:
Use o seguinte comando para descobrir seu ID
```
docker ps
```
E pare-o usando 
```
docker stop <ID do contêiner>
```

## Para mais informações sobre actions, confira:  
https://rasa.com/docs/rasa/actions  
https://rasa.com/docs/action-server/running-action-server  
https://www.youtube.com/watch?v=t_Ds4uT2z5g&t=601s