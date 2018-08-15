from actions.actions_geral import ActionMultiline

class ActionExplicarPrazo(ActionMultiline):
    messages = [
        'Nesta etapa posso responder suas dúvidas a respeito de Datas '
        'e Prazos do seu projeto. Como: envio do CNAE e desistência de recurso',

        # 'O que você quer saber?'
    ]

class ActionPrazoEnvioCnae(ActionMultiline):
    messages = [
        'O proponente tem o prazo de 40 dias para responder a diligência '
        '20+20 prorrogados automaticamente. ',

        'Não é necessário fazer solicitação. ',

        'Caso seja insuficiente, o proponente poderá anexar o protocolo da '
        'Receita de inserção do CNAE no Salic.'
    ]

class ActionPrazoDesistirRecurso(ActionMultiline):
    messages = [
        'A partir do momento em que seu projeto foi enquadrado, iniciou-se o '
        'prazo de 10 dias corridos para recorrer ao enquadramento proposto '
        'para o projeto',

        'Caso concorde com o enquadramento dado é possível desistir desse '
        'prazo',

        'Ambas as manifestações se dão por via da aba "recurso" no Menu ao '
        'lado esquerdo da tela do projeto, no Salic'
    ]
