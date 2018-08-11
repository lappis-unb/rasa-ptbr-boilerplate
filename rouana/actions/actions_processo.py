from actions.actions_geral import ActionMultiline

class ActionExplicarProcesso(ActionMultiline):
    messages = [
        'Na categoria de processos eu posso responder dúvidas à respeito '
        'do fluxo de submissão do seu projeto.',

        'Por exemplo, você pode me fazer perguntar à respeito de captação '
        'de verbas ou sobre o estado do seu projeto.',

        'O que você gostaria de saber?'
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

class ActionProcessoCadastroProponente(ActionMultiline):
    messages = [
        'Basta você entrar no Salic...',

        'clicar em Administrativo > Cadastrar proponente',

        'e preencher todos os dados =)'
    ]

class ActionProcessoPedidoReativacao(ActionMultiline):
    messages = [
        'O pedido de reativação deve ser encaminhado através de PDF e assinado pelo proponente.',

        'O pedido deve conter as devidas justificativas para a reanálise do indeferimento e a resposta'
        'da diligência. E-mail para encaminhamento: reativacao.proposta@cultura.gov.br'
    ]
