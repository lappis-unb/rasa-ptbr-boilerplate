import re
import spacy

from rasa_core.actions.action import Action
from rasa_core.events import UserUtteranceReverted


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





class ActionAviso(ActionMultiline):
    messages = [
        'Para eu ser mais eficiente na solução da sua dúvida vou fazer algumas perguntas.\n'

        'Você já preencheu uma proposta? (Sim ou Não)',
    ]

class ActionIntroduzirExecucao(ActionMultiline):
    messages = [
        'Eu ainda não aprendi a falar sobre um projeto que está em Execução ou'
        'em Prestação de Contas. Ainda estou aprendendo... '
        'Em breve eu poderei responder sua dúvida. '
        'Neste momento, eu recomendo que vocẽ entre em contato com as equipes da SEFIC:\n'

        'Execução: acompanhamento.incentivo@cultura.gov.br\n'

        'Prestação de Contas: prestacaodecontas.incentivo@cultura.gov.br\n'
    ]

class ActionJaEhProponente(ActionMultiline):
    messages = [
        'Você já tem um proponente cadastrado? (Sim ou Não)',
    ]

class ActionCadastroProponenteIntroduzirContexto(ActionMultiline):
    messages = [
        'Maravilha!\n'
        'Agora eu posso tentar esclarer algumas de suas dúvidas',
    ]

class ActionCadastroSalicVideo(ActionMultiline):
    messages = [
        'O Salic é o Sistema de Apoio às Leis de Incentivo à Cultura, e é por '
        'ele que você cadastra a proposta e a acompanha\n'

        'Se você encontrar dificuldades no momento do cadastro, pode assistir '
        'este vídeo, nele você pode observar o passo a passo para se cadastrar:',

        'https://youtu.be/rMGEZyIr1U8',

        'Caso você não possa ver o vídeo, eu posso te explicar. Quer que eu te explique? (Sim ou Não)'
    ]

class ActionExplicarCadastroSalic(ActionMultiline):
    messages = [
        'A primeira coisa que você deve fazer é acessar o SALIC no site http://salic.cultura.gov.br\n'

        'Então no formulário inicial, onde pede login e senha, você deve'
        'clicar na opção "Não sou cadastrado", logo abaixo\n'

        'Preencha todos os campos corretamente, todos eles são obrigatórios.'
        'E depois clique em "Cadastrar"\n'

        'Agora aguarde a chegada de um e-mail de confirmação. Este vai conter '
        'uma senha temporária\n'

        'É interessante você alterar esta senha, por isso, no seu primeiro '
        'acesso, vá em "Usuário > Alterar Senha", para mudar a mesma',

        'Agora que você já se cadastrou, o próximo passo cadastrar um proponente'
    ]

class ActionCadastroSalicAposVideo(ActionMultiline):
    messages = [
        'Espero que o vídeo tenha ajudado\n'
        'Agora que você já se cadastrou, o próximo passo cadastrar um proponente'
    ]

class ActionInscricaoProponente(ActionMultiline):
    messages = [
        'Para inscrever um proponente, ou se tornar um proponente, você deve:\n'

        'Acessar o SALIC e efetuar o login\n'

        'Clique em Administrativo e depois em cadastrar proponente. OU acesse esse link http://salic.cultura.gov.br/agente/agentes/incluiragente;',

        'Se você for uma pessoa física você precisa atuar na área cultural.'
        ' Caso você seja uma pessoa jurídica pública tem que atuar na área de administração indireta ou uma pessoa jurídica privada com ou sem fins lucrativos.'
    ]

class ActionIntroduzirContextoNovaProposta(ActionMultiline):
    messages = [
        'Que bom! É sempre bom trabalhar em novos projetos culturais\n'

        'Se você quiser, posso tirar algumas de suas dúvidas para te ajudar neste novo projeto'
    ]

class ActionIntroduzirContextoNaoExecucao(ActionMultiline):
    messages = [
        'Então suas dúvidas devem ser sobre as outras etapas do processo\n'

        'Vamos saná-las juntos? (Sim ou Não)'
    ]

class ActionMaisAlgumaPergunta(ActionMultiline):
    messages = [
        'Você possui mais alguma dúvida? (Sim ou Não)',
    ]

class ActionMaisPerguntasAfirmativa(ActionMultiline):
    messages = [
        'Que bom! Espero estar ajudando',
    ]

class ActionEscolheuContextoErrado(ActionMultiline):
    messages = [
        'Talvez sua dúvida esteja em alguma das outras áreas',
    ]

class ActionExplicarContextos(ActionMultiline):
    messages = [
        'Na categoria "Processo" eu responderei a respeito '
        'do fluxo de submissão do seu projeto, e o sobre o estado dele.\n'

        'Em "Preenchimento" eu vou tirar dúvidas sobre o '
        'preenchimento de propostas no Salic, campos em que você possa ter '
        'dúvidas, ou como você pode preencher\n'

        'Agora, em Datas e Prazos, eu consigo falar sobre prazos importantes '
        'para a aceitação e execução do seu projeto.\n'

        'Por último, em erros do SALIC, posso falar sober eventuais erros que '
        'ocorrem durante a utilização do sistema.',

        'Já que te expliquei, vou te dar as opçẽs de novo '
    ]

class ActionExtra(ActionMultiline):
    messages = [
        '=)'
    ]

class ActionAindaNaoAprendi(ActionMultiline):
    messages = [
        'Eu ainda não aprendi a falar sobre este tópico...\n'

        'Em breve eu poderei responder sua dúvida\n'

        'Neste momento, eu recomendo que vocẽ entre em contato com as equipes da SEFIC: http://rouanet.cultura.gov.br/fale-conosco/',
    ]

class ActionRevert(Action):
    def name(self):
        return "action_revert"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Sorry, didn't get that. Try again.")
        return [UserUtteranceReverted()]
