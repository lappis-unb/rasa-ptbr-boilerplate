from rouana.actions.actions_geral import ActionMultiline

## Ações de Fluxo

class ActionCuriosidadesIndicacao(ActionMultiline):
    messages = [
        'Legal! Meu assunto favorito :wink:',
        'Você pode me perguntar algumas curiosidades sobre a Lei Rouanet',
        'Por exemplo, o que é a Lei Rouanet, ou de onde vem o dinheiro usado na Lei.',
        'Qual a sua pergunta? Vou tentar responder da melhor maneira possível :smiley:',
    ]

class ActionCuriosidadesMais(ActionMultiline):
    messages = [
        'Gostaria de saber mais curiosidades?'
    ]

class ActionCuriosidadesMaisSim(ActionMultiline):
    messages = [
        'Que bom! :smiley:',
        'O que mais você gostaria de saber?',
    ]

class ActionCuriosidadesMaisNao(ActionMultiline):
    messages = [
        'Ok, podemos conversar sobre projetos e propostas',
        'Você quer falar sobre isso?',
    ]

class ActionCuriosidadesFalarSobreProjetos(ActionMultiline):
    messages = [
        'Maravilha! É bom saber que você quer entender mais sobre propostas e projetos :smiley:',
    ]

class ActionCuriosidadesFim(ActionMultiline):
    messages = [
        'Espero que eu tenha sido de grande ajuda',
        'Ainda estou em fase de teste, a cada dia aprenderei mais com sua ajuda',
        'Até mais! :wave:'
    ]



## Curiosidades Gerais

class ActionCuriosidadesQuantidadeProjetos(ActionMultiline):
    messages = [
        'Até o momento foram enviadas mais de 240.000 propostas, das quais mais de 89.000 foram aprovadas, se tornando projetos.',
        'Há mais de 43.000 proponentes cadastrados e mais de 80.000 incentivadores contribuindo com projetos.',
        '- Além disso, mais de 69.000 fornecedores foram contratados pelos proponentes.',
    ]

class ActionCuriosidadesBeneficiosIncentivoProjetosCulturais(ActionMultiline):
    messages = [
        'O principal benefício de incentivar projetos culturais é dar a chance para sociedade usufruir das mais diversas manifestações culturais que talvez nunca fossem possíveis sem incentivo.',
        'E tem mais...as empresas que incentivam projetos culturais podem deduzir do imposto de renda as quantias que despenderam em projetos aprovados pelo Ministério da Cultura',
        'É claro que essa dedução do imposto de renda acontece nas condições estabelecidas na legislação vigente, e está limitada a 4% do imposto devido',
    ]

class ActionCuriosidadesLeiRouanetElegibilidade(ActionMultiline):
    messages = [
        'Todo projeto cultural, de qualquer artista, produtor e agente cultural brasileiro, pode se beneficiar desta Lei e se candidatar à captação de recursos de renúncia fiscal.',
        'A proponência pode ser feita por Pessoas físicas com atuação comprovada na área cultural, ou Pessoas jurídicas de natureza cultural com, no mínimo, dois anos de atividade,',
        'podendo ser:',
        'Pessoas jurídicas públicas da administração indireta',
        '(autarquias, fundações culturais etc.)',
        'ou pessoas jurídicas privadas com ou sem fins lucrativos',
        '(empresas, cooperativas, fundações, ONGs, organizações culturais etc.)',
    ]

class ActionCuriosidadesLeiRouanetArrecadamento(ActionMultiline):
    messages = [
        'O mecanismo de incentivos fiscais da Lei Rouanet é uma forma de estimular o apoio da iniciativa privada ao setor cultural.',
        'Ou seja, o governo abre mão de parte dos impostos, para que esses valores sejam investidos na Cultura.',
        'Qualquer empresa tributada com base no lucro real, e pessoas físicas pagadoras de Imposto de Renda (IR) que fazem a declaração no modelo completo podem contribuir com a lei Rouanet apoiando projetos.',
        'Atualmente, mais de 3 mil projetos são apoiados a cada ano por meio desta lei.',
    ]

class ActionCuriosidadesLeiRouanetDenuncia(ActionMultiline):
    messages = [
        'Para denunciar um projeto suspeito de irregularidades é preciso registrar uma denúncia para o Ministério Público Federal.',
        'Sua denúncia pode ser feita no site do ministério público no link: http://aplicativos.pgr.mpf.mp.br/ouvidoria/portal/cadastro.html?tipoServico=2 ,ou pelo aplicativo do MPF na opção de "Registrar denúncia ou solicitação".',
    ]

class ActionCuriosidadesElegibilidadeDeEmpresaParaBeneficios(ActionMultiline):
    messages = [
        'Somente as Pessoas Jurídicas tributadas com base no Lucro Real podem descontar as doações ou patrocínios do imposto de renda observando sempre o limite máximo de 4% do imposto devido se você quiser saber mais sobre quais Pessoas Jurídicas devem fazer a apuração do lucro real confira o artigo 246, do Decreto 3.000 de 26 de março de 1999 que “Regulamenta a tributação, fiscalização, arrecadação e administração do Imposto sobre a Renda e Proventos de Qualquer Natureza”',
    ]

class ActionCuriosidadesQualPapelMinc(ActionMultiline):
    messages = [
        'Para que um projeto seja aprovado uma proposta deve ser cadastrada junto ao Ministério da Cultura onde a proposta passa por um exame de admissibilidade, que diz respeito à viabilidade técnica da atividade a ser realizada.',
        'Uma vez que a proposta seja aprovada, ela se transformará em um projeto (com um número de Pronac). O projeto, por sua vez, precisa ser aprovado por uma das unidades técnicas vinculadas ao Ministério da Cultura.',
        'Após o parecer do Ministério da Cultura, o projeto ainda é submetido à CNIC que irá aprová-lo ou indeferi-lo',
    ]

class ActionCuriosidadesReceberIncetivoDeParentes(ActionMultiline):
    messages = [
        'Olha, alguns familiares não podem incentivar projetos:',
        '- o cônjuge',
        '- os parentes até o terceiro grau, inclusive os afins',
        '- e os dependentes… tanto do doador, quanto do patrocinador, dos titulares, administradores, acionistas ou sócios de pessoa jurídica vinculada ao doador ou patrocinador, na data da operação, ou nos 12 meses anteriores.',
    ]

class ActionCuriosidadesPapelMinc(ActionMultiline):
    messages = [
        'Para que um projeto seja aprovado uma proposta deve ser cadastrada junto ao Ministério da Cultura onde a proposta passa por um exame de admissibilidade, que diz respeito à viabilidade técnica da atividade a ser realizada.',
        'Uma vez que a proposta seja aprovada, ela se transformará em um projeto (com um número de Pronac). O projeto, por sua vez, precisa ser aprovado por uma das unidades técnicas vinculadas ao Ministério da Cultura.',
        'Após o parecer do Ministério da Cultura, o projeto ainda é submetido à CNIC que irá aprová-lo ou indeferi-lo.',
    ]

class ActionCuriosidadesDeducaoImpostoDeRendaIncentivador(ActionMultiline):
    messages = [
        'Atualmente, existem 2 situações descritas na Lei 8313/91:',
        '1) o artigo 26 da Lei indica que os percentuais de dedução do IR são os seguintes:',
        'Empresas:',
        'até 30% do valor patrocinado;',
        'até 40% do valor doado',
        'Pessoa física:',
        'até 60% do valor patrocinado;',
        'até 80% do valor doado.',
        'nesse caso, a empresa incentivadora poderá ainda lançar o valor incentivado como despesa operacional',
        '2) Com a modificação implementada pela Lei 9.874/99, quem investe em projetos culturais enquadrados nos segmentos indicados pelo artigo 18 da Lei passou a ter a possibilidade de deduzir até 100% do valor doado ou patrocinado as empresas que investem nesses segmentos não podem lançar o valor incentivado como despesa operacional agora, IMPORTANTE:',
        'os percentuais de dedução de IR são limitados aos estabelecidos pela legislação do imposto de renda vigente, que atualmente são 4% do imposto devido para empresas e 6% do imposto devido para pessoa física',
        'Você pode ver os detalhes das leis pelos endereços:',
        'Lei 8313/91: http://www.planalto.gov.br/ccivil_03/leis/l8313cons.htm',
        'Lei 9.874/99: http://www.planalto.gov.br/ccivil_03/leis/l9874.htm',
    ]

class ActionCuriosidadesComoEhFeitaDeducaoImpostoDeRenda(ActionMultiline):
    messages = [
        'A dedução é feita no momento do pagamento do imposto, ao fim do período fiscal do recolhimento. Ou seja, a empresa deixa de pagar à União a parcela da doação ou patrocínio, subtrai o valor do imposto apurado e recolhe para a União, por meio de DARF, apenas o imposto devido após a dedução do incentivo. No caso de pessoas físicas, a dedução será feita do imposto a pagar na declaração anual do Imposto de Renda',
    ]

class ActionCuriosidadesDescontoDoIrDasDoecoes(ActionMultiline):
    messages = [
        'Não, as transferências a título de doações ou patrocínios não estão sujeitas à incidência do imposto de renda na fonte',
    ]

