from rasa_core.actions.action import Action


class ActionOQueEh(Action):
    dont_know_message = 'Desculpe, não sei conceituar isso ainda'
    meaning_map = {
        'a12': [
            'O estado A12 acontece durante a fase de Admissibilidade, e significa aguarda complementação de documentos',
            'E quando o MinC utiliza ele? Quando se solicita ao proponente documentação adicional',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 69.',
        ],
        'a14': [
            'O estado A14 acontece durante a fase de Admissibilidade, e significa indeferido – não enquadramento nos objetivos e fins da Lei 8313/91 ou do Decreto 5761/06',
            'E quando o MinC utiliza ele? Quando o projeto não se enquadra nos objetivos e fins do Art. 1º da Lei 8313/1991',
            'Para saber mais você pode consultar a Lei 8.313/1991, Art. 1º Instrução Normativa 05/2017, Art. 23',
        ],
        'a20': [
            'O estado A20 acontece durante a fase de Admissibilidade, e significa indeferido – projeto em duplicidade',
            'E quando o MinC utiliza ele? Quando se constata que se trata de projeto idêntico a ser realizado no mesmo período',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 23, I, b)',
        ],
        'a23': [
            'O estado A23 acontece durante a fase de Admissibilidade, e significa indeferido – somatório dos projetos apresentados excede o limite permitiddo para pessoa física',
            'E quando o MinC utiliza ele? Quando o somatório dos projetos apresentados execede os limites trazidos no Art. 20 da Instrução Normativa MinC nº 1/2017',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 4',
        ],
        'b01': [
            'O estado B01 acontece durante a fase de Admissibilidade, e significa proposta transformada em projeto',
            'E quando o MinC utiliza ele? Após o exame de admissibilidade',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 24 e 25',
        ],
        'b02': [
            'O estado B02 acontece durante a fase de Admissibilidade, e significa projeto enquadrado',
            'E quando o MinC utiliza ele? Após o exame de admissibilidade o projeto é enquadrado no artigo 18 ou 26 da Lei 8313/91.',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 24',
        ],
        'b14': [
            'O estado B14 acontece durante a fase de Admissibilidade, e significa diligenciado – Parecer técnico',
            'E quando o MinC utiliza ele? Quando da necessidade de informações adicionais para fins de análise técnica',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 69',
        ],
        'a13': [
            'O estado A13 acontece durante a fase de Aprovação, e significa arquivado – solicitação de desistência do proponente',
            'E quando o MinC utiliza ele? ',
            'Para saber mais você pode consultar a ',
        ],
        'a16': [
            'O estado A16 acontece durante a fase de Aprovação, e significa indeferido – Projeto já realizado.',
            'E quando o MinC utiliza ele? ',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 23, I, b)',
        ],
        'a17': [
            'O estado A17 acontece durante a fase de Aprovação, e significa indeferido – não atendimento à diligência',
            'E quando o MinC utiliza ele? Quando o proponente não atende a alguma diligência feita',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 69, § 3º',
        ],
        'a42': [
            'O estado A42 acontece durante a fase de Aprovação, e significa projeto arquivado – não atendimento à diligência técnica',
            'E quando o MinC utiliza ele? Quando o proponente não atende a alguma diligência feita',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 69, § 3º',
        ],
        'b11': [
            'O estado B11 acontece durante a fase de Aprovação, e significa encaminhado para análise técnica',
            'E quando o MinC utiliza ele? Situação em que o projeto é encaminhado para análise na vinculada.',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 26, §2º e Art. 27',
        ],
        'b20': [
            'O estado B20 acontece durante a fase de Aprovação, e significa projeto adequado à realidade de execução',
            'E quando o MinC utiliza ele? Antes de ser encaminhado para análise técnica, o proponente tem a prerrogativa de promover ajustes, visando adequar o projeto à realidade da execução.',
            'Para saber mais você pode consultar a Instrução Normativa 05/201, Art. 26',
        ],
        'c09': [
            'O estado C09 acontece durante a fase de Aprovação, e significa projeto fora da pauta – Proponente Inabilitado',
            'E quando o MinC utiliza ele? Quando o proponente encontra-se inabilitado, seus projetos em fase de aprovação, são tirados de pauta.',
            'Para saber mais você pode consultar a Instrução Normativa 05/201, Art. 59',
        ],
        'c10': [
            'O estado C10 acontece durante a fase de Aprovação, e significa projeto incluído em pauta para avaliação da CNIC',
            'E quando o MinC utiliza ele? Após conclusão da análise técnica, o projeto é incluido na pauta da CNIC',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 28',
        ],
        'c20': [
            'O estado C20 acontece durante a fase de Aprovação, e significa parecer técnico emitido',
            'E quando o MinC utiliza ele? Quando ocorre a conclusão da análise e o parecer técnico é emitido',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 27',
        ],
        'c26': [
            'O estado C26 acontece durante a fase de Aprovação, e significa projeto incluído na pauta da CNIC para reanálise/análise complementar',
            'E quando o MinC utiliza ele? Quando autoridade superior entende que algum item pode ser reavaliado ou quando constatado erro material',
            'Para saber mais você pode consultar a STF, Súmula nº 346/1963 (autotutela)',
        ],
        'c30': [
            'O estado C30 acontece durante a fase de Aprovação, e significa diligenciado – Comissão Nacional de Incentivo à Cultura – CNIC',
            'E quando o MinC utiliza ele? Quando da necessidade de informações adicionais para fins de análise técnica',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 69',
        ],
        'd03': [
            'O estado D03 acontece durante a fase de Aprovação, e significa projeto aprovado – aguardando análise documental',
            'E quando o MinC utiliza ele? Após análise da CNIC.',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 28',
        ],
        'd14': [
            'O estado D14 acontece durante a fase de Aprovação, e significa indeferido',
            'E quando o MinC utiliza ele? Quando o projeto é indeferido',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017',
        ],
        'd20': [
            'O estado D20 acontece durante a fase de Aprovação, e significa recurso',
            'E quando o MinC utiliza ele? Quando o proponente interpõe recurso contra resultado da análise',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 67',
        ],
        'd25': [
            'O estado D25 acontece durante a fase de Aprovação, e significa diligenciado – Projeto aprovado – (Solicitação de Documentos)',
            'E quando o MinC utiliza ele? Quando da necessidade de informações adicionais para fins de aprovação',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 69',
        ],
        'd27': [
            'O estado D27 acontece durante a fase de Aprovação, e significa encaminhado para inclusão em portaria',
            'E quando o MinC utiliza ele? Quando o projeto é encaminhado para publicação em portaria no Diário Oficial da União',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 25',
        ],
        'e25': [
            'O estado E25 acontece durante a fase de Avaliação do objeto, e significa análise de resposta de diligência – Objeto',
            'E quando o MinC utiliza ele? O proponente respodeu à diligência enviada e a resposta aguarda análise do técnico',
            'Para saber mais você pode consultar a Portaria Interministerial nº 424/2016, art. 59, III',
        ],
        'e62': [
            'O estado E62 acontece durante a fase de Avaliação do objeto, e significa diligenciado – na avaliação do relatório cumprimento de objeto',
            'E quando o MinC utiliza ele? Proponente foi diligenciado na análise do objeto.',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, art. 47, §3º',
        ],
        'e66': [
            'O estado E66 acontece durante a fase de Avaliação do objeto, e significa inadimplente – por não responder diligência na avaliação do relatório cumprimento de objeto',
            'E quando o MinC utiliza ele? O proponente foi diligenciado na análise do objeto e não apresentou resposta no prazo correto.',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, art. 58, I',
        ],
        'e20': [
            'O estado E20 acontece durante a fase de Avaliação financeira, e significa inadimplente – não respondeu a diligência da Prestação de Contas',
            'E quando o MinC utiliza ele? Quando o proponente é omisso em responder à diligência.',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, art. 69, § 3º, inc. III',
        ],
        'e27': [
            'O estado E27 acontece durante a fase de Avaliação financeira, e significa análise Financeira da Prestação de Contas',
            'E quando o MinC utiliza ele? Quando se inicia a análise financeira da prestação de contas.',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, art. 50',
        ],
        'e30': [
            'O estado E30 acontece durante a fase de Avaliação financeira, e significa análise de resposta de diligência',
            'E quando o MinC utiliza ele? Quando se inicia a análise financeira da resposta à diligência.',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, art. 69',
        ],
        'e68': [
            'O estado E68 acontece durante a fase de Avaliação financeira, e significa aguarda análise financeira',
            'E quando o MinC utiliza ele? Quando o projeto aguarda o início da análise financeira da prestação de contas.',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, art. 50',
        ],
        'e77': [
            'O estado E77 acontece durante a fase de Avaliação financeira, e significa aguarda laudo final',
            'E quando o MinC utiliza ele? Quando a avaliação de resultados está finalizada e aguarda a produção do laudo final.',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, art. 53',
        ],
        'l03': [
            'O estado L03 acontece durante a fase de Avaliação financeira, e significa prestação de contas aprovada com ressalva formal e sem prejuízo',
            'E quando o MinC utiliza ele? Quando a prestação de contas é aprovada com ressalva.',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, art. 51, inc. II e art. 53',
        ],
        'l05': [
            'O estado L05 acontece durante a fase de Avaliação financeira, e significa prestação de contas desaprovada com notificação de cobrança',
            'E quando o MinC utiliza ele? Quando a prestação de contas é reprovada, é dada a ciência ao proponente por intimação.',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, art. 54, § 5°',
        ],
        'l08': [
            'O estado L08 acontece durante a fase de Avaliação financeira, e significa prestação de contas aprovada após ressarcimento ao erário.',
            'E quando o MinC utiliza ele? Quando a prestação de contas é reprovada, mas o proponente reverte com o ressarcimento do débito ao FNC.',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, art. 59, § 3°',
        ],
        'l10': [
            'O estado L10 acontece durante a fase de Avaliação financeira, e significa prestação de contas reprovada – Inabilitação Prescrita',
            'E quando o MinC utiliza ele? Quando são transcorridos cinco anos após a prestação de contas do projeto, a inabilitação prescreve.',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, art. 57',
        ],
        'l11': [
            'O estado L11 acontece durante a fase de Avaliação financeira, e significa prestação de contas reprovada – Inabilitação suspensa',
            'E quando o MinC utiliza ele? Quando a justiça manda suspender a inabilitação do proponente.',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, art. 59',
        ],
        'd22': [
            'O estado D22 acontece durante a fase de Execução, e significa aguardando elaboração de portaria de Prorrogação',
            'E quando o MinC utiliza ele? Quando há prorrogação automática ou proponente solicita prorrogação de prazo',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, art. 33',
        ],
        'd28': [
            'O estado D28 acontece durante a fase de Execução, e significa encaminhado p/inclusão em portaria/complementação',
            'E quando o MinC utiliza ele? Quando o projeto atinge o percentual de 50% de captação, pode solicitar complementação orçamentária',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 38',
        ],
        'd29': [
            'O estado D29 acontece durante a fase de Execução, e significa encaminhado p/inclusão em portaria/redução.',
            'E quando o MinC utiliza ele? Quando o projeto atinge o percentual de 20% de captação, pode solicitar redução orçamentária',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 39',
        ],
        'e10': [
            'O estado E10 acontece durante a fase de Execução, e significa autorizada a captação total dos recursos',
            'E quando o MinC utiliza ele? Quando é publicada a autorização para captação de recursos',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 33',
        ],
        'e11': [
            'O estado E11 acontece durante a fase de Execução, e significa expirado o prazo de captação total',
            'E quando o MinC utiliza ele? Quando expira o prazo de captação',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 33',
        ],
        'e12': [
            'O estado E12 acontece durante a fase de Execução, e significa autorizada a captação residual dos recursos',
            'E quando o MinC utiliza ele? Quando o projeto já obteve alguma captação e ainda se encontra com prazo vigente',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, art. 33',
        ],
        'e13': [
            'O estado E13 acontece durante a fase de Execução, e significa projeto em execução – Encerrado prazo de captação',
            'E quando o MinC utiliza ele? Quando o prazo de captação expirou, mas o prazo de execução continua vigente.',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, arts. 33 e 34',
        ],
        'e15': [
            'O estado E15 acontece durante a fase de Execução, e significa expirado o prazo de captação parcial',
            'E quando o MinC utiliza ele? Quando o projeto atingiu captação suficiente para movimentar e o prazo de captação expira.',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, art. 33',
        ],
        'e16': [
            'O estado E16 acontece durante a fase de Execução, e significa projeto encerrado por excesso de prazo sem captação',
            'E quando o MinC utiliza ele? Situação automática: quando o projeto não consegue captar recursos suficientes para liberação das contas e o prazo expira',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, art. 52',
        ],
        'e23': [
            'O estado E23 acontece durante a fase de Execução, e significa inadimplente',
            'E quando o MinC utiliza ele? Situação que gira automaticamente quando o proponente não apresenta a prestação de contas final dentro do prazo regular',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, art. 48, §1°',
        ],
        'e24': [
            'O estado E24 acontece durante a fase de Execução, e significa apresentou prestação de contas',
            'E quando o MinC utiliza ele? Quando a prestação de contas é apresentada, é recebida pela GCEFI e o projeto é, posteriormente, tramitado para a CGARE',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, art. 49',
        ],
        'e36': [
            'O estado E36 acontece durante a fase de Execução, e significa arquivado por ter 24 meses aprovação sem captação de recursos',
            'E quando o MinC utiliza ele? Quando ocoore o arquivamento porque o projeto atingiu 24 meses sem captação nenhuma',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, art. 52',
        ],
        'e59': [
            'O estado E59 acontece durante a fase de Execução, e significa diligenciado – Readequação',
            'E quando o MinC utiliza ele? Quando o proponente pleitea alterações e é diligenciado para apresentar documentos/informações complementares',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Arts. 29 a 31',
        ],
        'e63': [
            'O estado E63 acontece durante a fase de Execução, e significa projeto arquivado – por excesso de prazo sem captação',
            'E quando o MinC utiliza ele? Quando o proponente não solicitou a prorrogação do período de captação de forma tempestiva',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 52',
        ],
        'e64': [
            'O estado E64 acontece durante a fase de Execução, e significa projeto arquivado – captação/execução encerradas',
            'E quando o MinC utiliza ele? Quando o pedido de prorrogação é indeferido por se tratar de calendário específico',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 52',
        ],
        'e65': [
            'O estado E65 acontece durante a fase de Execução, e significa projeto arquivado – solicitação de arquivamento, de projeto de incentivo fiscal, feito pelo proponente',
            'E quando o MinC utiliza ele? Quando o arquivamento ocorre a pedido do proponente',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 52',
        ],
        'e75': [
            'O estado E75 acontece durante a fase de Execução, e significa expirado o prazo de execução do projeto',
            'E quando o MinC utiliza ele? Quando expira o prazo de execução e inicia-se o prazo para entrega da prestação de contas final',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Arts. 48 e 49',
        ],
        'e79': [
            'O estado E79 acontece durante a fase de Execução, e significa projeto não executado por insuficiência de captação de recursos',
            'E quando o MinC utiliza ele? Situação automática: criada para projetos que não captaram recursos suficientes para iniciar a execução',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 52',
        ],
        'e80': [
            'O estado E80 acontece durante a fase de Execução, e significa inadimplente – Proponente notificado a apresentar prestação de contas',
            'E quando o MinC utiliza ele? Situação criada para diligenciar automaticamente o proponente que não entregou a prestação de contas final dentro do prazo regular',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 48, §1º',
        ],
        'e81': [
            'O estado E81 acontece durante a fase de Execução, e significa inadimplente – Não atendeu a notificação para apresentar prestação de contas',
            'E quando o MinC utiliza ele? Situação automática: criada para que os projetos, cujos proponentes não apresentaram a prestação de contas final depois de terem sido notificados, sejam encaminhados para TCE.',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 48, §1º',
        ],
        'e60': [
            'O estado E60 acontece durante a fase de Fiscalização, e significa diligenciado – fiscalização',
            'E quando o MinC utiliza ele? Quando é necessário que o proponente apresente documentos ou informações para a Coordenação de Fiscalização.',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 69',
        ],
        'e72': [
            'O estado E72 acontece durante a fase de Fiscalização, e significa execução Suspensa de Forma Cautelar',
            'E quando o MinC utiliza ele? Após decisão da autoridade máxima da Secretaria em casos que são detectados indícios de irregularidades no projeto',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, Art. 58, II',
        ],
        'e50': [
            'O estado E50 acontece durante a fase de Movimentação Financeira, e significa diligenciado – movimentação da conta corrente',
            'E quando o MinC utiliza ele? Quando constata-se alguma inconsistência bancária ou na transferência de recursos e o proponente é diligenciado para prestar esclarecimentos.',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, arts. 80 a 83',
        ],
        'l09': [
            'O estado L09 acontece durante a fase de Parcelamento, e significa débito Parcelado',
            'E quando o MinC utiliza ele? Quando o proponente realiza o pagamento da primeira parcela do parcelamento solicitado, independentemente da situação em que o processo se encontre',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, art. 64',
        ],
        'd38': [
            'O estado D38 acontece durante a fase de Recomposição de dano ao erário, e significa cADIN – Inadimplente',
            'E quando o MinC utiliza ele? Após a situação E78, quando a inscrição no Cadin é realizada',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, art. 56',
        ],
        'e22': [
            'O estado E22 acontece durante a fase de Recomposição de dano ao erário, e significa instaurada Tomada de Contas Especial',
            'E quando o MinC utiliza ele? Após a situação G47, quando a tomada de contas especial é instaurada',
            'Para saber mais você pode consultar a IN TCU 71/2012, art. 4º',
        ],
        'e73': [
            'O estado E73 acontece durante a fase de Recomposição de dano ao erário, e significa tCE julgada pelo TCU',
            'E quando o MinC utiliza ele? Atualização dos autos e do Salic após o julgamento das contas pelo TCU',
            'Para saber mais você pode consultar a ',
        ],
        'e78': [
            'O estado E78 acontece durante a fase de Recomposição de dano ao erário, e significa débito inferior ao valor mínimo para TCE',
            'E quando o MinC utiliza ele? Após asituação L06, quando o processo segue para análise e instrução à tomada de contas simplificada',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, art. 56',
        ],
        'g47': [
            'O estado G47 acontece durante a fase de Recomposição de dano ao erário, e significa em processo de instauração de Tomada de Contas Especial',
            'E quando o MinC utiliza ele? Após asituação L06, quando o processo segue para análise e instrução à tomada de contas especial',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, art. 56',
        ],
        'l06': [
            'O estado L06 acontece durante a fase de Recomposição de dano ao erário, e significa prestação de contas desaprovada com INDICATIVO para Tomada de Contas Especial',
            'E quando o MinC utiliza ele? Após a situação L05',
            'Para saber mais você pode consultar a Instrução Normativa 05/2017, art. 56',
        ],
        'rouana': [
            'Uma assistente virtual, como eu, é um programa de computador criado para ajudar as pessoas a sanarem suas dúvidas de maneira simples',
            'Apesar de eu ser um "computador", eu ainda estou aprendendo várias coisas para poder te ajudar melhor',
            'Conversando comigo você também pode me ajudar a alcançar isso',
        ],
        'lei rouanet': [
            'A Lei 8.313/91, conhecida como Lei Rouanet, é o principal '
            'mecanismo de fomento à Cultura do Brasil. Ela instituiu o '
            'Programa Nacional de Apoio à Cultura (Pronac).',

            'O nome Rouanet remete a seu criador, o então secretário Nacional '
            'de Cultura, o diplomata Sérgio Paulo Rouanet.',

            'A Lei estabelece as normativas de como o Governo Federal deve '
            'disponibilizar recursos para a realização de projetos '
            'artístico-culturais.',

            '"A Lei foi concebida originalmente com três mecanismos: o Fundo '
            'Nacional da Cultura (FNC), o Incentivo Fiscal e o Fundo de '
            'Investimento Cultural e Artístico (Ficart). Este nunca foi '
            'implementado, enquanto o Incentivo Fiscal – também chamado de '
            'mecenato – prevaleceu e chega ser confundido com a própria Lei."',
        ],
        'minc': [
             'O Ministério da Cultura (MinC) é o responsável pela aprovação e '
             'monitoramento dos projetos submetidos para captação.'
        ],
        'sefic': [
             'A (Secretaria de Fomento e Incentivo à Cultura) planeja, '
             'coordena e supervisiona a operacionalização do Programa '
             'Nacional de Apoio à Cultura (Pronac), na aprovação, '
             'monitoramento e prestação de contas de projetos culturais.'
        ],
        'projeto': [
             'Projeto é o termo dado para a proposta aprovada no SALIC.'
        ],
        'proposta': [
             'Proposta é o conjunto de formulários que explicam o projeto '
             'cultural que pode ser incentivado pela Lei Rouanet.'
        ],
        'proponente': [
             'Proponente é o agente responsável por propor e participar '
             'de projetos culturais.'
        ],
        'preechimento': [
             'É a primeira fase da proposta, onde você preenche os formulários.'
        ],
        'admissibilidade': [
             'É a fase da proposta em que o MinC e a vinculada irão avaliar a '
             'proposta, para pedir correções ou aprova-la, gerando um projeto.'
        ],
        'aprovação': [
             'Aprovação é a fase onde o MinC e a vinculada estão julgando a validade do '
             'projeto'
        ],
        'execução': [
             'Execução é a fase referente ao andamento do projeto '
             'que possue atividades como captação de recursos e realização do projeto.'
        ],
        'prestação de contas': [
             'É a fase realizada no final do projeto, onde o proponente '
             'deve apresentar todas as notas fiscais e contratos realizados '
             'afim de provar o gasto correto do recurso.'
        ],
        'salic': [
             'Sistema de Apoio às Leis de Incentivo à Cultura (SALIC) é o '
             'sistema utilizado para submeter propostas e gerenciar os '
             'projetos aprovados pela Lei Rouanet.',

             'Você pode acessa-lo aqui: salic.cultura.gov.br'
        ],
        'vinculada': [
             'As vinculadas são órgãos associados ao MinC especialistas nas '
             'áreas específicas que a Lei Rouanet cobre.',

             'Elas que avaliam o orçamento e adequação do projeto.'
        ],
    }

    def name(self):
        return 'action_o_que_eh'

    def run(self, dispatcher, tracker, domain):
        user_message = tracker.latest_message.text.lower()

        for word in self.meaning_map:
            if word in user_message:
                for message in self.meaning_map[word]:
                    dispatcher.utter_message(message)

                return []

        dispatcher.utter_message(self.dont_know_message)
        return []
