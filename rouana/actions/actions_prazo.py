from actions.actions_geral import ActionMultiline

class ActionExplicarPrazo(ActionMultiline):
    messages = [
        'Então vamos falar sobre prazo.'
    ]

class ActionPrazoEnvioCnae(ActionMultiline):
    messages = [
        'O proponente tem o prazo de 40 dias para responder a diligência 20+20 prorrogados automaticamente.'
        'Não é necessário fazer solicitação.',
        'Caso seja insuficiente, o proponente poderá anexar o protocolo da Receita de inserção do CNAE no Salic.',
    ]