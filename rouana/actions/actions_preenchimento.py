from actions.actions_geral import ActionMultiline

class ActionExplicarPreenchimento(ActionMultiline):
    messages = [
        'Vamos falar sobre preenchimento. '
    ]

class ActionExplicarPlanilhaDesaparecida(ActionMultiline):
    messages = [
        'Ao excluir um produto do plano de distribuição a planilha vai ser '
        '"zerada" e o proponente deverá refazê-la novamente.'
    ]
