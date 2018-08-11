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
        'Oi eu sou a Rouana, assistente virtual do minc, e estou aqui para te ajudar a '
        'esclarecer dúvidas sobre a Lei Rouanet',

        'e também solucionar problemas de proposta e projeto'
    ]

class ActionDefinirPerfil(ActionMultiline):
    messages = [

        'Você prefere conversar sobre criação e andamento de projetos, ou '

        'prefere falar mais sobre a Lei Rouanet? :smile:'
    ]

class ActionNovaProposta(ActionMultiline):
    messages = [
        'Você já começou a trabalhar em uma nova proposta de projeto?'
    ]

class ActionDuvidaExecucao(ActionMultiline):
    messages = [
        'Você tem dúvida em relação à captação de verba e execução do '
        'projeto?'
    ]

class ActionConheceProcesso(ActionMultiline):
    messages = [
        'Você sabe como funciona o andamento de um projeto de incentivo a '
        'cultura?'
    ]

class ActionCadastroSalic(ActionMultiline):
    messages = [
        'Você já tem cadastro no SALIC?'
    ]

class ActionDespedir(ActionMultiline):
    messages = [
        'Espero que eu tenha conseguido esclarecer suas dúvidas',

        'Ainda estou em fase de teste, a cada dia aprendo mais com as conversas que tenho com vocês',

        'Se surgir alguma dúvida, não hesite, volte aqui',

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
        'Tá bom!'
        'Onde sua pergunta se encaixa melhor:',
        '1. Processo e estado do projeto',
        '2. Preenchimento de proposta',
        '3. Datas e Prazos',
        '4. Erros do SALIC',
        '5. Não sei bem onde se encaixa',
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
        'em Prestação de Contas. Ainda estou aprendendo...',

        'Em breve eu poderei responder sua dúvida :wink:',

        'Neste momento, eu recomendo que vocẽ entre em contato com as equipes da SEFIC:',

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
        'Agora eu posso tentar esclarer algumas de suas dúvidas',
    ]

class ActionCadastroSalicVideo(ActionMultiline):
    messages = [
        'O Salic é o Sistema de Apoio às Leis de Incentivo à Cultura, e é por '
        'ele que você cadastra a proposta e a acompanha',

        'Se você encontrar dificuldades no momento do cadastro, pode assistir este vídeo',

        'Nele você pode observar o passo a passo para se cadastrar:'

        'https://youtu.be/rMGEZyIr1U8',

        'Caso você não possa ver o vídeo, eu posso te explicar',

        'Quer que eu te explique? :smiley:'
    ]

class ActionExplicarCadastroSalic(ActionMultiline):
    messages = [
        'A primeira coisa que você deve fazer é acessar o SALIC no site http://salic.cultura.gov.br',

        'Então no formulário inicial, onde pede login e senha, você deve'
        'clicar na opção "Não sou cadastrado", logo abaixo',

        'Preencha todos os campos corretamente, todos eles são obrigatórios.'
        'E depois clique em "Cadastrar"',

        'Agora aguarde a chegada de um e-mail de confirmação. Este vai conter'
        'uma senha temporária',

        'É interessante você alterar esta senha, por isso, no seu primeiro '
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

        'Acessar o SALIC e efetuar o login',

        'Clique em Administrativo e depois em cadastrar proponente. OU acesse esse link http://salic.cultura.gov.br/agente/agentes/incluiragente;',

        'Se você for uma pessoa física você precisa atuar na área cultural.'
        ' Caso você seja uma pessoa jurídica pública tem que atuar na área de administração indireta ou uma pessoa jurídica privada com ou sem fins lucrativos.'
    ]

class ActionIntroduzirContextoNovaProposta(ActionMultiline):
    messages = [
        'Que bom!É sempre bom trabalhar em novos projetos culturais',

        'Se você quiser, posso tirar algumas de suas dúvidas para te ajudar neste novo projeto'
    ]

class ActionIntroduzirContextoNaoExecucao(ActionMultiline):
    messages = [
        'Então suas dúvidas devem ser sobre as outras etapas do processo',

        'Vamos saná-las juntos? :smiley:'
    ]

class ActionMaisAlgumaPergunta(ActionMultiline):
    messages = [
        'Você possui mais alguma dúvida?',
    ]

class ActionMaisPerguntasAfirmativa(ActionMultiline):
    messages = [
        'Que bom! Espero estar ajudando :smiley:',
    ]

class ActionEscolheuContextoErrado(ActionMultiline):
    messages = [
        'Talvez sua dúvida esteja em alguma das outras áreas :thinking_face:',
    ]

class ActionExplicarContextos(ActionMultiline):
    messages = [
        'Na categoria "Processo" eu responderei a respeito '
        'do fluxo de submissão do seu projeto, e o sobre o estado dele.',

        'Em "Preenchimento" eu vou tirar dúvidas sobre o '
        'preenchimento de propostas no Salic, campos em que você possa ter '
        'dúvidas, ou como você pode preencher',

        'Agora, em Datas e Prazos, eu consigo falar sobre prazos importantes '
        'para a aceitação e execução do seu projeto.',

        'Por último, em erros do SALIC, posso falar sober eventuais erros que '
        'ocorrem durante a utilização do sistema.',

        'Já que te expliquei, vou te dar as opçẽs de novo :smiley: '
    ]
