from actions.actions_geral import ActionMultiline

class ActionExplicarPreenchimento(ActionMultiline):
    messages = [
        'Vamos falar sobre preenchimento. '
    ]

class ActionPreenchimentoPlanilhaDesaparecida(ActionMultiline):
    messages = [
        'Ao excluir um produto do plano de distribuição a planilha vai ser '
        '"zerada" e o proponente deverá refazê-la.'
    ]

class ActionPreenchimentoCampoCustoAuditoria(ActionMultiline):
    messages = [
        'Não precisa preencher esse campo agora :wink:'
    ]

class ActionPreenchimentoVinculoDePropostas(ActionMultiline):
    messages = [
        'Você deve ir em:',
        'Orçamento do projeto > Custos por produto > Clicar no produto desejado',
        'Clicar no Local de realização > por último na aba Assessoria contábil e jurídica.'
    ]

class ActionPreenchimentoValorIngresso(ActionMultiline):
    messages = [
        'Esse valor é usado para conferir a viabilidade do projeto e não pode ultrapassar R$ 250,00 por beneficiário.',
        'Por exemplo: R$ 9.445.076,00 / 22.556 pessoas = R$ 419,18 por beneficiário, ou seja, está acima do limite para sanar esse problema,' 
        'você pode diminuir o custo do projeto ou aumentar a estimativa de público.'
    ]

class ActionPreenchimentoVinculoCpfProposta(ActionMultiline):
    messages = [
        'O dirigente do projeto deve acessar o sistema e seguir os passos:'
        '1- Administrativo > Gerenciar responsáveis'
            'em seguida...', 
        '2- Vincular propostas > Clicar na "bolinha" (Vincular) > Inserir responsável > abaixo terá o número da Proposta/Nome' 
            '> Nome do responsável selecionado > Clicar na "bolinha"',
        '3- Por último... clica também no botão Vincular'

    ]

class ActionPreenchimentoErroSalvamento(ActionMultiline):
    messages = [
        'Esse erro aconteceu por exceder o tempo logado no sistema.'
        'O limite de tempo para o preenchimento da proposta é de 20 minutos.'
        'Não esqueça de ir salvando a cada passo do preenchimento.'
    ]

class ActionPreenchimentoErroVinculoCpfCnpj(ActionMultiline):
    messages =[
        'Apenas o dirigente da instituição é quem pode vincular uma pessoa física ao CNPJ'
        'o dirigente deve entrar com login e senha e aceitar o vínculo'
    ]

class ActionPreenchimentoErroAcharProposta(ActionMultiline):
    messages = [
        'Selecione o CPF ou CNPJ que deseja como proponente e liste a proposta do CPF ou CNPJ selecionado  para isso, vá em:',
        '1- Proposta > Listar proposta',
        '2- Clicar em CPF Proponente > Selecionar o CNPJ aparecerão todas as propostas ativas no sistema'
    ]