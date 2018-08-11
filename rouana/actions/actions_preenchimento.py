from actions.actions_geral import ActionMultiline

class ActionExplicarPreenchimento(ActionMultiline):
    messages = [
        'Nesta etapa eu posso responder dúvidas sobre o preenchimento de '
        'propostas no SALIC',

        'O que você gostaria de saber?'
    ]

class ActionPreenchimentoCampoCustoAuditoria(ActionMultiline):
    messages = [
        'Não precisa preencher esse campo agora'
    ]

class ActionPreenchimentoVinculoDePropostas(ActionMultiline):
    messages = [
        'Você deve ir em:',

        'Orçamento do projeto > Custos por produto > Clicar no produto '
        'desejado',

        'Clicar no Local de realização > por último na aba Assessoria '
        'contábil e jurídica.'
    ]

class ActionPreenchimentoValorIngresso(ActionMultiline):
    messages = [
        'Esse valor é usado para conferir a viabilidade do projeto e não '
        'pode ultrapassar R$ 250,00 por beneficiário.',

        'Por exemplo: R$ 9.445.076,00 / 22.556 pessoas = R$ 419,18 por '
        'beneficiário, ou seja, está acima do limite para sanar esse problema,',

        'você pode diminuir o custo do projeto ou aumentar a estimativa '
        'de público.'
    ]

class ActionPreenchimentoVinculoCpfProposta(ActionMultiline):
    messages = [
        'O dirigente do projeto deve acessar o sistema e seguir os passos:'
        '1- Administrativo > Gerenciar responsáveis'
            'em seguida...',

        '2- Vincular propostas > Clicar na "bolinha" (Vincular) > Inserir '
        'responsável > abaixo terá o número da Proposta/Nome '
            '> Nome do responsável selecionado > Clicar na "bolinha"',

        '3- Por último... clica também no botão Vincular'
    ]

class ActionPreenchimentoAgenciaBancaria(ActionMultiline):
    messages = [
        'A agência bancária deve ser do banco do Brasil, deve conter 5 '
        'dígitos, sem hifens, pontos ou letras',
    ]
