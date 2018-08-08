from actions.actions_geral import ActionMultiline

class ActionExplicarProcesso(ActionMultiline):
    messages = [
        'Na categoria de processos eu posso responder dúvidas à respeito '
        'do fluxo de submissão do seu projeto.',

        'Por exemplo, você pode me fazer perguntar à respeito de captação '
        'de verbas ou sobre o estado do seu projeto.',

        'O que você gostaria de saber?'
    ]

class ActionProcessoProjetoHomologado(ActionMultiline):
    messages = [
        'Um projeto homologado (estado D52) recebeu uma posição definitiva '
        'ou seja, é um projeto que foi aprovado ou não',

        'aí, um termo de homologação é anexado ao projeto '
        'para o proponente verificar e se manifestar a respeito',

        'caso não concorde com a homologação, '
        'o proponente pode encaminhar um pedido de reconsideração para '
        'proposta.incentivo@cultura.gov.br',

        'ou, caso concorde, '
        'pode avisar que não quer entrar com recurso (também pelo proposta. '
        'incentivo@cultura.gov.br) '
        'o prazo para recursos é de 10 dias corridos a partir da data de '
        'homologação',

        'ah, muito importante... o proponente que quiser se manifestar '
        'deve enviar o e-mail a partir do mesmo endereço que está '
        'cadastrado no projeto'
    ]

class ActionProcessoCaptacaoDeRecursos(ActionMultiline):
    messages = [
        'A captação só pode começar depois que o projeto passa pela fase de '
        'enquadramento, pela análise documental e pela publicação.',

        'Assim que o projeto é publicado no Diário Oficial da União você pode '
        'começar a captar recursos.'
    ]

class ActionProcessoReativacaoDeProposta(ActionMultiline):
    messages = [
        'Pra reativar uma proposta indeferida você deve enviar '
        'um pedido de reativação',

        'esse pedido tem que expor as justificativas apropriadas para '
        'reanálise e deve ser assinado pelo proponente',

        'você encaminha o pedido em formato PDF para '
        'reativacao.proposta@cultura.gov.br',

        'e aí é só aguardar uma resposta =)'
    ]

class ActionProcessoProjetoAdequacao(ActionMultiline):
    messages = [
        'Um projeto liberado para adequação (estado E90) '
        'é um projeto que garantiu o mínimo de 10% do seu valor...',

        'e que agora pode ser adequado conforme a sua realidade',

        'se você quiser saber como dar prosseguimento ao projeto sem fazer '
        'alterações, escreva “prosseguir com e90”',

        'ou, para entender como fazer alterações e o que pode ser alterado, '
        'escreva “alterar e90”'
    ]

class ActionProcessoCadastroProponente(ActionMultiline):
    messages = [
        'Basta você entrar no Salic...',

        'clicar em Administrativo > Cadastrar proponente',

        'e preencher todos os dados =)'
    ]
