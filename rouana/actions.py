from rasa_core.actions.action import Action

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

class ActionMultiline(Action):
    messages = ['']

    def name(self):
        return self.__class__.__name__

    def run(self, dispatcher, tracker, domain):
        for message in self.messages:
            dispatcher.utter_message(message)
        return []

class ActionSubmissaoDeProjetos(ActionMultiline):
    messages = [
        'Tudo bem. Aqui vai um resumo do processo:',
        'A pessoa responsável, chamada de proponente, insere uma proposta cultural no Sistema de Apoio às Leis de Incentivo à Cultura (Salic), de forma eletrônica.',
        'Essa proposta é analisada pelo MinC. Se for aprovada, autoriza o proponente a captar recursos.',
        'Assim que o valor mínimo for captado, o proponente pode começar a executar o projeto.',
        'Durante a execução o proponente deve prestar contas de acordo com os prazos definidos na Lei Rouanet.',
        'A prestação de contas é analisada pelos técnicos do Ministério e se aprovada, permite que o proponente crie um novo projeto.',
    ]

class ActionDefinirContexto(ActionMultiline):
    messages = [
        'Entendi.',
        'Então, onde sua pergunta se encaixa melhor:',
        '1. Processo e estado do projeto',
        '2. Preenchimento do Salic',
        '3. Datas e Prazos',
        '4. Erros do SALIC',
        '5. Não sei bem onde se encaixa',
    ]

class ActionAviso(ActionMultiline):
    messages = [
        'Tudo bem, para eu ser mais eficiente na solução da sua dúvida vou fazer algumas perguntas.',
        'Você já preencheu uma proposta?',
    ]

class ActionIntroduzirExecucao(ActionMultiline):
    messages = [
        'Olha, você pode perguntar sobre:',
        'Planilha orçamentária',
        'Prestação de contas',
        'Captação',
        'Mas, por enquanto, eu ainda não consigo responder sobre esses assuntos :cry::cry:',
    ]

