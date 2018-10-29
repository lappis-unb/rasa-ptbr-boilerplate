from actions.actions_geral import ActionMultiline

## Ações de Fluxo

class ActionCuriosidadesIndicacao(ActionMultiline):
    messages = [
        'Legal! Meu assunto favorito',
        'Você pode me perguntar algumas curiosidades sobre a Lei Rouanet\n'
        'Por exemplo, o que é a Lei Rouanet, ou de onde vem o dinheiro usado na Lei.\n'
        'Qual a sua pergunta? Vou tentar responder da melhor maneira possível',
    ]

class ActionCuriosidadesMais(ActionMultiline):
    messages = [
        'Gostaria de saber mais curiosidades? (Sim ou Não)'
    ]

class ActionCuriosidadesMaisSim(ActionMultiline):
    messages = [
        'Que bom!',
        'O que mais você gostaria de saber?',
    ]

class ActionCuriosidadesMaisNao(ActionMultiline):
    messages = [
        'Ok, podemos conversar sobre projetos e propostas\n'
        'Você quer falar sobre isso? (Sim ou Não)',
    ]

class ActionCuriosidadesFalarSobreProjetos(ActionMultiline):
    messages = [
        'Maravilha! É bom saber que você quer entender mais sobre propostas e projetos',
    ]


## Curiosidades Gerais

class ActionCuriosidadesQuantidadeProjetos(ActionMultiline):
    messages = [
        'Até o momento foram enviadas mais de 240.000 propostas, das quais mais de 89.000 foram aprovadas, se tornando projetos.\n'
        'Há mais de 43.000 proponentes cadastrados e mais de 80.000 incentivadores contribuindo com projetos.\n'
        'Além disso, mais de 69.000 fornecedores foram contratados pelos proponentes.',
    ]

class ActionCuriosidadesBeneficiosIncentivoProjetosCulturais(ActionMultiline):
    messages = [
        'O principal benefício de incentivar projetos culturais é dar a chance para sociedade usufruir das mais diversas manifestações culturais que talvez nunca fossem possíveis sem incentivo.\n'
        'E tem mais...as empresas que incentivam projetos culturais podem deduzir do imposto de renda as quantias que despenderam em projetos aprovados pelo Ministério da Cultura\n'
        'É claro que essa dedução do imposto de renda acontece nas condições estabelecidas na legislação vigente, e está limitada a 4% do imposto devido',
    ]

class ActionCuriosidadesLeiRouanetElegibilidade(ActionMultiline):
    messages = [
        'Todo projeto cultural, de qualquer artista, produtor e agente cultural brasileiro, pode se beneficiar desta Lei e se candidatar à captação de recursos de renúncia fiscal.\n'
        'A proponência pode ser feita por Pessoas físicas com atuação comprovada na área cultural, ou Pessoas jurídicas de natureza cultural com, no mínimo, dois anos de atividade,\n'
        'podendo ser:',
        'Pessoas jurídicas públicas da administração indireta\n'
        '(autarquias, fundações culturais etc.)\n'
        'ou pessoas jurídicas privadas com ou sem fins lucrativos\n'
        '(empresas, cooperativas, fundações, ONGs, organizações culturais etc.)',
    ]

class ActionCuriosidadesLeiRouanetArrecadamento(ActionMultiline):
    messages = [
        'O mecanismo de incentivos fiscais da Lei Rouanet é uma forma de estimular o apoio da iniciativa privada ao setor cultural.\n'
        'Ou seja, o governo abre mão de parte dos impostos, para que esses valores sejam investidos na Cultura.\n'
        'Qualquer empresa tributada com base no lucro real, e pessoas físicas pagadoras de Imposto de Renda (IR) que fazem a declaração no modelo completo podem contribuir com a lei Rouanet apoiando projetos.\n'
        'Atualmente, mais de 3 mil projetos são apoiados a cada ano por meio desta lei.',
    ]

class ActionCuriosidadesLeiRouanetDenuncia(ActionMultiline):
    messages = [
        'Em caso de dúvida, entrar em contato com as áreas do MinC, http://rouanet.cultura.gov.br/fale-conosco/ .\n',
    ]

class ActionCuriosidadesElegibilidadeDeEmpresaParaBeneficios(ActionMultiline):
    messages = [
        'Somente as Pessoas Jurídicas tributadas com base no Lucro Real podem descontar as doações ou patrocínios do imposto de renda observando sempre o limite máximo de 4% do imposto devido \n' 
        'Se você quiser saber mais sobre quais Pessoas Jurídicas devem fazer a apuração do lucro real confira o artigo 246, do Decreto 3.000 de 26 de março de 1999 que “Regulamenta a tributação, fiscalização, arrecadação e administração do Imposto sobre a Renda e Proventos de Qualquer Natureza”',
    ]

class ActionCuriosidadesReceberIncetivoDeParentes(ActionMultiline):
    messages = [
        'Olha, alguns familiares não podem incentivar projetos:\n'
        '- o cônjuge\n'
        '- os parentes até o terceiro grau, inclusive os afins\n'
        '- e os dependentes… tanto do doador, quanto do patrocinador, dos titulares, administradores, acionistas ou sócios de pessoa jurídica vinculada ao doador ou patrocinador, na data da operação, ou nos 12 meses anteriores.',
    ]

class ActionCuriosidadesDeducaoImpostoDeRendaIncentivador(ActionMultiline):
    messages = [
        'Atualmente, existem 2 situações descritas na Lei 8313/91:\n'
        '1) o artigo 26 da Lei indica que os percentuais de dedução do IR são os seguintes:',
        'Empresas:\n'
        'até 30% do valor patrocinado;\n'
        'até 40% do valor doado\n'
        'Pessoa física:\n'
        'até 60% do valor patrocinado;\n'
        'até 80% do valor doado.\n'
        'nesse caso, a empresa incentivadora poderá ainda lançar o valor incentivado como despesa operacional',
        '2) Com a modificação implementada pela Lei 9.874/99, quem investe em projetos culturais enquadrados nos segmentos indicados pelo artigo 18 da Lei passou a ter a possibilidade de deduzir até 100% do valor doado ou patrocinado as empresas que investem nesses segmentos não podem lançar o valor incentivado como despesa operacional agora, IMPORTANTE:\n'
        'os percentuais de dedução de IR são limitados aos estabelecidos pela legislação do imposto de renda vigente, que atualmente são 4% do imposto devido para empresas e 6% do imposto devido para pessoa física',
        'Você pode ver os detalhes das leis pelos endereços:\n'
        'Lei 8313/91: http://www.planalto.gov.br/ccivil_03/leis/l8313cons.htm\n'
        'Lei 9.874/99: http://www.planalto.gov.br/ccivil_03/leis/l9874.htm',
    ]

class ActionCuriosidadesValorMaximoProjeto(ActionMultiline):
    messages = [
        'Isto depende do seu perfil de proponente.\n',
        'Sobre qual perfil você quer saber:\n'
        '- Pessoa Física e Microempresário Individual(MEI)\n'
        '- Demais Pessoas Jurídicas\n'
        '- Quero saber de todos'
    ]

class ActionCuriosidadesValorMaximoPessoaFisica(ActionMultiline):
    messages = [
        'Para a Pessoa Física e para o Empresário Individual com enquadramento em Microempresário Individual (MEI), o valor máximo é de R$ 1,5 milhão para até quatro projetos por ano.\n',
        'Estes limites podem ser ultrapassados dependendo do espaço em que o projeto cultural será realizado e a região:\n'
        'Ocorrendo em espaço público, estes perfis tem a quantidade de projetos acrescido em 2, mas o valor máximo não muda.'
    ]

class ActionCuriosidadesValorMaximoPessoaJuridica(ActionMultiline):
    messages = [
        'Em realção aos demais enquadramentos de Empresário Individual, o valor máximo é de R$ 7,\5 milhões para até oito projetos por ano;'
        'Para a Empresa Individual de Responsabilidade Limitada (EIRELI), Sociedades Limitadas (Ltda.) e demais Pessoas Jurídicas, o valor máximo é de R$ 60 milhões para até 16 projetos por ano.\n'
        'Se o projeto cultural ocorrer em espaço público, o Empresário Individual tem a quantidade de projetos acrescido em 3, mas o valor máximo não muda.\n'
        'Ássim como as Empresa Individual de Responsabilidade Limitada (EIRELI), Sociedades Limitadas (Ltda.) e demais Pessoas Jurídicas, quem podem somar mais 4 projetos, se realizados em espaço público, mantendo os limites orçamentários.'
    ]
