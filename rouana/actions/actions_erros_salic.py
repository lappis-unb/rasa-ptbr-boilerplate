from actions.actions_geral import ActionMultiline

class ActionExplicarErrosSalic(ActionMultiline):
    messages = [
        'Nesta etapa eu posso responder dúvidas sobre eventuais erros do '
        'sistema SALIC. Como: planilha desaparecida, perda dos dados '
        'preenchidos e recuperação de senha',

        'O que você gostaria de saber?'
    ]

class ActionErroSalicPlanilhaDesaparecida(ActionMultiline):
    messages = [
        'Ao excluir um produto do plano de distribuição a planilha vai ser '
        '"zerada" e o proponente deverá refazê-la.'
    ]

class ActionErroSalicErroSalvamento(ActionMultiline):
    messages = [
        'Esse erro aconteceu por exceder o tempo logado no sistema.'
        'O limite de tempo para o preenchimento da proposta é de 20 minutos.'
        'Não esqueça de ir salvando a cada passo do preenchimento.'
    ]

class ActionErroSalicRecuperacaoDeSenha(ActionMultiline):
    messages = [
        'Ah isso acontece com todo mundo ;) ',

        'você pode gerar uma nova senha aqui: '
        'http://salic.cultura.gov.br/autenticacao/index/solicitarsenha',

        'ou se isso não funcionar, mande uma solicitação para: '
        'senhasalic@cultura.gov.br'
    ]
