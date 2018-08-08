from actions.actions_geral import ActionMultiline

class ActionExplicarCorrecao(ActionMultiline):
    messages = [
        'Estamos na etapa de correção, aqui posso responder dúvidas '
        'de campos preenchidos incorretamente ou motivos para sua proposta '
        'não ser aceita. Vou tentar te ajudar a corrigí-los.',

        'Mas, por enquanto, eu não consigo te responder a respeito deste '
        'assunto.'
    ]

