from rasa_core.actions.action import Action
from rasa_core.actions.forms import FormAction, EntityFormField, BooleanFormField, FreeTextFormField
from rasa_core.events import SlotSet

# print(tracker.latest_message)
# print(tracker.latest_bot_utterance)
# print(tracker.latest_action_name)
# print(domain.templates)
# print(domain.intents)

class ActionWhatIs(Action):
    def name(self):
        return 'action_what_is'

    def run(self, dispatcher, tracker, domain):
        word_template_map = {
            'proponente': 'Um proponente é bla bla bla bla bla',
            'banana': 'Banana é uma fruta amarela =)',
        }

        user_message = tracker.latest_message.text

        for word in word_template_map:
            if word in user_message:
                dispatcher.utter_message(word_template_map[word])
                return []
        dispatcher.utter_message('Desculpe, não sei conceituar isso ainda =/')
        return []

class ActionSetSlotTrue(Action):
    def name(self):
        return 'action_set_slot_true'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('eh_propenete = True')
        return [SlotSet("eh_propenete", True)]

class ActionSetSlotFalse(Action):
    def name(self):
        return 'action_set_slot_false'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('eh_propenete = False')
        return [SlotSet("eh_propenete", False)]

class ActionIndicacaoCuriosidades(Action):
    def name(self):
        return 'action_indicacao_curiosidades'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('Tá bom! A partir de agora, você pode perguntar informações sobre a Lei, dinheiro dos projetos ou o que é necessário fazer para submeter um projeto?')
        dispatcher.utter_message('Vou tentar responder da melhor maneira possível :smiley:')
        return []


class ActionDefinicaoLei(Action):
    def name(self):
        return 'action_definicao_lei'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('A Lei 8.313/91, conhecida como Lei Rouanet, é o principal mecanismo de fomento à Cultura do Brasil. Ela instituiu o Programa Nacional de Apoio à Cultura (Pronac).')
        dispatcher.utter_message('O nome Rouanet remete a seu criador, o então secretário Nacional de Cultura, o diplomata Sérgio Paulo Rouanet.')
        dispatcher.utter_message('A Lei estabelece as normativas de como o Governo Federal deve disponibilizar recursos para a realização de projetos artístico-culturais.')
        dispatcher.utter_message('"A Lei foi concebida originalmente com três mecanismos: o Fundo Nacional da Cultura (FNC), o Incentivo Fiscal e o Fundo de Investimento Cultural e Artístico (Ficart). \
        Este nunca foi implementado, enquanto o Incentivo Fiscal – também chamado de mecenato – prevaleceu e chega ser confundido com a própria Lei."')
        return []


class ActionQuantidadeProjetos(Action):
    def name(self):
        return 'action_quantidade_projetos'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('Até o momento foram enviadas mais de 240.000 propostas, das quais mais de 89.000 foram aprovadas, se tornando projetos.')
        dispatcher.utter_message('Além disso, mais de 69.000 fornecedores foram contratados pelos proponentes.')
        dispatcher.utter_message('Há mais de 43.000 proponentes cadastrados e mais de 80.000 incentivadores contribuindo com projetos.')
        return []

class ActionArrecadacaoLei(Action):
    def name(self):
        return 'action_arrecadacao_lei'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(' O mecanismo de incentivos fiscais da Lei Rouanet é uma forma de estimular o apoio da iniciativa privada ao setor cultural. \
         Ou seja, o governo abre mão de parte dos impostos, para que esses valores sejam investidos na Cultura.')
        dispatcher.utter_message('Qualquer empresa tributada com base no lucro real, e pessoas físicas pagadoras de Imposto de Renda (IR) que fazem a declaração no modelo completo \
          podem contribuir com a lei Rouanet apoiando projetos.')
        dispatcher.utter_message('Atualmente, mais de 3 mil projetos são apoiados a cada ano por meio desta lei.')
        return []

class ActionSubmissaoDeProjetos(Action):
    def name(self):
        return 'action_submissao_de_projeto'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('Tudo bem. Aqui vai um resumo do processo:')
        dispatcher.utter_message('A pessoa responsável, chamada de proponente, insere uma proposta cultural no Sistema de Apoio às Leis de Incentivo à Cultura (Salic), de forma eletrônica.')
        dispatcher.utter_message('Essa proposta é analisada pelo MinC. Se for aprovada, autoriza o proponente a captar recursos.')
        dispatcher.utter_message('Assim que o valor mínimo for captado, o proponente pode começar a executar o projeto.')
        dispatcher.utter_message('Durante a execução o proponente deve prestar contas de acordo com os prazos definidos na Lei Rouanet.')
        dispatcher.utter_message('A prestação de contas é analisada pelos técnicos do Ministério e se aprovada, permite que o proponente crie um novo projeto.')
        dispatcher.utter_message('Você quer saber mais detalhes sobre essas etapas?')
        return []

class ActionDefinirContexto(Action):
    def name(self):
        return 'action_definir_contexto'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('Entendi.') 
        dispatcher.utter_message('Então, onde sua pergunta se encaixa melhor:')
        dispatcher.utter_message('1. Processo e estado do projeto')
        dispatcher.utter_message('2. Preenchimento do Salic')
        dispatcher.utter_message('3. Datas e Prazos')
        dispatcher.utter_message('4. Erros do SALIC')
        dispatcher.utter_message('5. Não sei bem onde se encaixa')
        return []

class ActionAviso(Action):
    def name(self):
        return 'action_aviso'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('Tudo bem, para eu ser mais eficiente na solução da sua dúvida vou fazer algumas perguntas.')
        dispatcher.utter_message('Você já preencheu uma proposta?')
        return []

class ActionIntroduzirExecucao(Action):
    def name(self):
        return 'action_introduzir_execucao'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('Olha, você pode perguntar sobre:')
        dispatcher.utter_message('Planilha orçamentária')
        dispatcher.utter_message('Prestação de contas')
        dispatcher.utter_message('Captação')
        dispatcher.utter_message('Mas, por enquanto, eu ainda não consigo responder sobre esses assuntos :cry::cry:')
        return []
