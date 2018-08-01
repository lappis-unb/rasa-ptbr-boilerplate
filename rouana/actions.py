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

class ActionIndicacaoCuriosidades(ActionMultiline):
    messages = [
        'Tá bom! A partir de agora, você pode perguntar informações sobre a '
        'Lei, dinheiro dos projetos ou o que é necessário fazer para submeter '
        'um projeto?',

        'Vou tentar responder da melhor maneira possível :smiley:'
    ]

class ActionDefinicaoLei(ActionMultiline):
    messages = [
        'A Lei 8.313/91, conhecida como Lei Rouanet, é o principal mecanismo '
        'de fomento à Cultura do Brasil. Ela instituiu o Programa Nacional de '
        'Apoio à Cultura (Pronac).',

        'O nome Rouanet remete a seu criador, o então secretário Nacional de '
        'Cultura, o diplomata Sérgio Paulo Rouanet.',

        'A Lei estabelece as normativas de como o Governo Federal deve '
        'disponibilizar recursos para a realização de projetos '
        'artístico-culturais.',

        '"A Lei foi concebida originalmente com três mecanismos: o Fundo '
        'Nacional da Cultura (FNC), o Incentivo Fiscal e o Fundo de '
        'Investimento Cultural e Artístico (Ficart). '
        'Este nunca foi implementado, enquanto o Incentivo Fiscal – também '
        'chamado de mecenato – prevaleceu e chega ser confundido com a própria'
        ' Lei."',
    ]


class ActionQuantidadeProjetos(ActionMultiline):
    messages = [
        'Até o momento foram enviadas mais de 240.000 propostas, das quais mais de 89.000 foram aprovadas, se tornando projetos.',
        'Além disso, mais de 69.000 fornecedores foram contratados pelos proponentes.',
        'Há mais de 43.000 proponentes cadastrados e mais de 80.000 incentivadores contribuindo com projetos.',
    ]

class ActionArrecadacaoLei(ActionMultiline):
    messages = [
        ' O mecanismo de incentivos fiscais da Lei Rouanet é uma forma de estimular o apoio da iniciativa privada ao setor cultural. Ou seja, o governo abre mão de parte dos impostos, para que esses valores sejam investidos na Cultura.',
        'Qualquer empresa tributada com base no lucro real, e pessoas físicas pagadoras de Imposto de Renda (IR) que fazem a declaração no modelo completo podem contribuir com a lei Rouanet apoiando projetos.',
        'Atualmente, mais de 3 mil projetos são apoiados a cada ano por meio desta lei.',
    ]

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
