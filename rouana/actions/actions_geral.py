import re
import spacy

from rasa_core.actions.action import Action


class ActionMultiline(Action):
    messages = ['']

    def name(self):
        return self.convert_name_to_snake_case()

    def run(self, dispatcher, tracker, domain):
        for message in self.messages:
            dispatcher.utter_message(message)
        return []

    def convert_name_to_snake_case(self):
        return re.sub('(.)([A-Z]{1})', r'\1_\2',
                      self.__class__.__name__).lower()

class ActionCumprimentar(ActionMultiline):
    messages = [
        'Oi eu sou a Rouana, assistente virtual do minc, e posso te ajudar a '
        'esclarecer dúvidas sobre a Lei Rouanet',

        'e também solucionar problemas de proposta e projeto'
    ]

class ActionDefinirPerfil(ActionMultiline):
    messages = [
        'Você quer conversar sobre criação e andamento de projetos? '
        'Ou, podemos falar mais sobre a Lei Rouanet'
    ]

class ActionNovaProposta(ActionMultiline):
    messages = [
        'Esta trabalhando em uma nova proposta?'
    ]

class ActionDuvidaExecucao(ActionMultiline):
    messages = [
        'Sua dúvida está relacionada com captação de verba e execução do '
        'projeto?'
    ]

class ActionConheceProcesso(ActionMultiline):
    messages = [
        'Você sabe como funciona todo o andamento de um projeto de incentivo a'
        ' cultura?'
    ]

class ActionCadastroSalic(ActionMultiline):
    messages = [
        'Tem cadastro no SALIC?'
    ]

class ActionDespedir(ActionMultiline):
    messages = [
        'Espero que eu tenha sido de grande ajuda',
        'Ainda estou em fase de teste, a cada dia aprenderei mais com sua ajuda',
        'Até mais! :wave:'
    ]

class ActionSubmissaoDeProjetos(ActionMultiline):
    messages = [
        'Tudo bem. Aqui vai um resumo do processo:',
        'A pessoa responsável, chamada de proponente, insere uma proposta cultural no Sistema de Apoio às Leis de Incentivo à Cultura (Salic), de forma eletrônica.',
        'Essa proposta é analisada pelo MinC. Se for aprovada, autoriza o proponente a captar recursos.',
        'Assim que o valor mínimo for captado, o proponente pode começar a executar o projeto.',
        'Durante a execução o proponente deve prestar contas de acordo com os prazos definidos na Lei Rouanet.',
        'A prestação de contas é analisada pelos técnicos do Ministério e se aprovada, permite que o proponente crie um novo projeto.',
        'O primeiro passo para você particiar deste processo é ter cadastro no SALIC'
    ]

class ActionDefinirContexto(ActionMultiline):
    messages = [
        'Onde sua pergunta se encaixa melhor:',
        '1. Processo e estado do projeto',
        '2. Preenchimento do Salic',
        '3. Datas e Prazos',
        '4. Correção de proposta enviada',
        '5. Erros do SALIC',
        '6. Não sei bem onde se encaixa',
    ]

class ActionAviso(ActionMultiline):
    messages = [
        'Para eu ser mais eficiente na solução da sua dúvida vou fazer algumas perguntas.',
        'Você já preencheu uma proposta?',
    ]

class ActionIntroduzirExecucao(ActionMultiline):
    messages = [
        ':disappointed_relieved:',

        'Eu ainda não aprendi a falar sobre um projeto que está em Execução ou'
        ' em Prestação de Contas. Porém eu ainda estou aprendendo, em um futuro'
        ' próximo eu saberei responder sua dúvida :wink:',

        'Por agora eu recomendo entrar em contato com as equipes da SEFIC',

        'Execução: acompanhamento.incentivo@cultura.gov.br',

        'Prestação de Contas: prestacaodecontas.incentivo@cultura.gov.br',
    ]

class ActionJaEhProponente(ActionMultiline):
    messages = [
        'Você já é um proponente cadastrado?',
    ]

class ActionCadastroProponenteIntroduzirContexto(ActionMultiline):
    messages = [
        'Maravilha!',
        'Então agora posso tentar esclarer algumas de suas dúvidas',
    ]

class ActionCadastroSalicVideo(ActionMultiline):
    messages = [
        'O Salic é o Sistema de Apoio às Leis de Incentivo à Cultura, e é por '
        'ele que você cadastra a proposta e a acompanha',

        'Olhe este vídeo para saber como você pode se cadastrar',

        'https://youtu.be/rMGEZyIr1U8',

        'Caso você não possa ver o vídeo, eu posso te explicar',

        'Quer que eu te explique? :smiley:'
    ]

class ActionExplicarCadastroSalic(ActionMultiline):
    messages = [
        'A primeira coisa que você deve fazer é acessar o SALIC, no site http://salic.cultura.gov.br',

        'Então no formulário inicial, onde pede login e senha, você deve '
        'clicar na opção "Não sou cadastrado", logo abaixo',

        'Preencha todos os campos corretamente, todos eles são obrigatórios. '
        'E depois clique em "Cadastrar"',

        'Agora aguarde a chegada de um e-mail de confirmação. Este vai conter '
        'uma senha temporária',

        'É altamente recomendado alterar esta senha, por isso, no seu primeiro '
        'acesso, vá em "Usuário > Alterar Senha", para mudar a mesma',

        'Agora que você já se cadastrou, o próximo passo é se tornar um proponente'
    ]

class ActionCadastroSalicAposVideo(ActionMultiline):
    messages = [
        'Espero que o vídeo tenha ajudado :smiley:',
        'Agora que você já se cadastrou, o próximo passo é se tornar um proponente'
    ]

class ActionInscricaoProponente(ActionMultiline):
    messages = [
        'Para inscrever um proponente, ou se tornar um proponente, você deve:',

        'Acessar o SALIC e efetuar o login;',

        'Clique em Administrativo e depois em cadastrar proponente. OU acesse esse link http://salic.cultura.gov.br/agente/agentes/incluiragente;',

        'Se você for uma pessoa física você precisa atuar na área cultural.'
        ' Caso você seja uma pessoa jurídica pública tem que atuar na área de administração indireta ou uma pessoa jurídica privada com ou sem fins lucrativos.'
    ]

class ActionIntroduzirContextoNovaProposta(ActionMultiline):
    messages = [
        'Que bom! Sempre é bom trabalhar em novos projetos culturais',

        'Posso tirar algumas dúvidas suas para te ajudar neste novo projeto'
    ]

class ActionIntroduzirContextoNaoExecucao(ActionMultiline):
    messages = [
        'Então suas dúvidas devem ser sobre as outras etapas do processo',

        'Posso tentar sanar elas :smiley:'
    ]

class ActionMaisAlgumaPergunta(ActionMultiline):
    messages = [
        'Você possui mais alguma dúvida?',
    ]

class ActionMaisPerguntasAfirmativa(ActionMultiline):
    messages = [
        'Que bom! Espero estar ajudando :smiley:',
    ]

class ActionExplicarContextos(ActionMultiline):
    messages = [
        'Como você está em dúvidas sobre o contexto, vou lhe explicar '
        'um pouco sobre o que é cada uma das categorias:',

        '1. Processo e estado do projeto: ',

        '2. Preenchimento do Salic: Dúvidas relacionadas ao preenchimento '
        'ou submissão de propostas no Salic.'
        ' Por exemplo, dúvidas no preenchimento de campos e utilização do '
        'sistema.'

        '3. Datas e prazos: '

        '4. Correção de proposta enviada: '

        '5. Erros do Salic: '
    ]
