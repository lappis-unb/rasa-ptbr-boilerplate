from rasa_core.actions.action import Action


class ActionOQueEh(Action):
    dont_know_message = 'Desculpe, não sei conceituar isso ainda :sad:'
    meaning_map = {
        'lei rouanet': [
            'A Lei 8.313/91, conhecida como Lei Rouanet, é o principal '
            'mecanismo de fomento à Cultura do Brasil. Ela instituiu o '
            'Programa Nacional de Apoio à Cultura (Pronac).',

            'O nome Rouanet remete a seu criador, o então secretário Nacional '
            'de Cultura, o diplomata Sérgio Paulo Rouanet.',

            'A Lei estabelece as normativas de como o Governo Federal deve '
            'disponibilizar recursos para a realização de projetos '
            'artístico-culturais.',

            '"A Lei foi concebida originalmente com três mecanismos: o Fundo '
            'Nacional da Cultura (FNC), o Incentivo Fiscal e o Fundo de '
            'Investimento Cultural e Artístico (Ficart). Este nunca foi '
            'implementado, enquanto o Incentivo Fiscal – também chamado de '
            'mecenato – prevaleceu e chega ser confundido com a própria Lei."',
        ],
        'minc': [
             'O Ministério da Cultura (MinC) é o responsável pela aprovação e '
             'monitoramento dos projetos submetidos para captação.'
        ],
        'sefic': [
             'A (Secretaria de Fomento e Incentivo à Cultura) planeja, '
             'coordena e supervisiona a operacionalização do Programa '
             'Nacional de Apoio à Cultura (Pronac), na aprovação, '
             'monitoramento e prestação de contas de projetos culturais.'
        ],
        'projeto': [
             'Projeto é o termo dado para a proposta aprovada no SALIC.'
        ],
        'proposta': [
             'Proposta é o conjunto de formulários que explicam o projeto '
             'cultural que pode ser incentivado pela Lei Rouanet.'
        ],
        'proponente': [
             'Proponente é o agente responsável por propor e participar '
             'de projetos culturais.'
        ],
        'preechimento': [
             'É a primeira fase da proposta, onde você preenche os formulários.'
        ],
        'admissibilidade': [
             'É a fase da proposta em que o MinC e a vinculada irão avaliar a '
             'proposta, para pedir correções ou aprova-la, gerando um projeto.'
        ],
        'execução': [
             'Execução é a fase referente ao andamento do projeto '
             'que possue atividades como captação de recursos e realização do projeto.'
        ],
        'prestação de contas': [
             'É a fase realizada no final do projeto, onde o proponente '
             'deve apresentar todas as notas fiscais e contratos realizados '
             'afim de provar o gasto correto do recurso.'
        ],
        'salic': [
             'Sistema de Apoio às Leis de Incentivo à Cultura (SALIC) é o '
             'sistema utilizado para submeter propostas e gerenciar os '
             'projetos aprovados pela Lei Rouanet.',

             'Você pode acessa-lo aqui: salic.cultura.gov.br'
        ],
        'vinculada': [
             'As vinculadas são órgãos associados ao MinC especialistas nas '
             'áreas específicas que a Lei Rouanet cobre.',

             'Elas que avaliam o orçamento e adequação do projeto.'
        ],
    }

    def name(self):
        return 'action_o_que_eh'

    def run(self, dispatcher, tracker, domain):
        user_message = tracker.latest_message.text.lower()

        for word in self.meaning_map:
            if word in user_message:
                for message in self.meaning_map[word]:
                    dispatcher.utter_message(message)

                return []

        dispatcher.utter_message(self.dont_know_message)
        return []
