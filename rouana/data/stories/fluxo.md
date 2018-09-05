## path
* cumprimentar
  - utter_cumprimentar
  - utter_definir_perfil
> identifica_perfil

## path-explicar-definicao-perfil
* cumprimentar
  - utter_cumprimentar
  - utter_definir_perfil
* negar
  - utter_explicar_definicao_perfil
> identifica_perfil


<!--- Fluxo Curiosidades --->

## path1
> identifica_perfil
* afirmar_curiosidades
  - utter_curiosidades_indicacao
> identificar_curiosidade

## path1.end.1
> curiosidade_final
* afirmar
  - utter_curiosidades_mais_sim
> identificar_curiosidade

## path1.end.2
> curiosidade_final
* negar
  - utter_curiosidades_mais_nao
> curiosidade_falar_sobre_projetos

## path1.end.2.1
> curiosidade_falar_sobre_projetos
* afirmar
  - utter_curiosidades_falar_sobre_projetos
  - utter_aviso
> identificar_preenchimento_de_proposta

## path1.end.2.2-fim
> curiosidade_falar_sobre_projetos
* negar
  - utter_despedir
  - utter_restart



<!--- Fluxos Propostas e Projetos --->

## path2
> identifica_perfil
* afirmar_projeto
  - utter_aviso
> identificar_preenchimento_de_proposta

## path2.1
> identificar_preenchimento_de_proposta
* afirmar
  - utter_nova_proposta
> identificar_nova_proposta

## path2.2
> identificar_preenchimento_de_proposta
* negar
  - utter_conhece_processo
> identificar_conhecimento_de_processo

## path2.3.oqueeh_estadoSalic{"estadoSalic":"A12"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_A12
> identificar_conhecimento_de_processo

## path2.4.oqueeh_estadoSalic{"estadoSalic":"A14"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_A14
> identificar_conhecimento_de_processo

## path2.5.oqueeh_estadoSalic{"estadoSalic":"A20"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_A20
> identificar_conhecimento_de_processo

## path2.6.oqueeh_estadoSalic{"estadoSalic":"A23"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_A23
> identificar_conhecimento_de_processo

## path2.7.oqueeh_estadoSalic{"estadoSalic":"B01"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_B01
> identificar_conhecimento_de_processo

## path2.8.oqueeh_estadoSalic{"estadoSalic":"B14"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_B14
> identificar_conhecimento_de_processo

## path2.9.oqueeh_estadoSalic{"estadoSalic":"A13"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_A13
> identificar_conhecimento_de_processo

## path2.10.oqueeh_estadoSalic{"estadoSalic":"A16"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_A16
> identificar_conhecimento_de_processo

## path2.11.oqueeh_estadoSalic{"estadoSalic":"A17"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_A17
> identificar_conhecimento_de_processo

## path2.12.oqueeh_estadoSalic{"estadoSalic":"A42"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_A42
> identificar_conhecimento_de_processo

## path2.13.oqueeh_estadoSalic{"estadoSalic":"B11"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_B11
> identificar_conhecimento_de_processo

## path2.14.oqueeh_estadoSalic{"estadoSalic":"B20"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_B20
> identificar_conhecimento_de_processo

## path2.15.oqueeh_estadoSalic{"estadoSalic":"C09"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_C09
> identificar_conhecimento_de_processo

## path2.16.oqueeh_estadoSalic{"estadoSalic":"C10"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_C10
> identificar_conhecimento_de_processo

## path2.17.oqueeh_estadoSalic{"estadoSalic":"C20"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_C20
> identificar_conhecimento_de_processo

## path2.18.oqueeh_estadoSalic{"estadoSalic":"C26"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_C26
> identificar_conhecimento_de_processo

## path2.19.oqueeh_estadoSalic{"estadoSalic":"C30"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_C30
> identificar_conhecimento_de_processo

## path2.20.oqueeh_estadoSalic{"estadoSalic":"D03"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_D03
> identificar_conhecimento_de_processo

## path2.21.oqueeh_estadoSalic{"estadoSalic":"D14"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_D14
> identificar_conhecimento_de_processo

## path2.22.oqueeh_estadoSalic{"estadoSalic":"D20"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_D20
> identificar_conhecimento_de_processo

## path2.23.oqueeh_estadoSalic{"estadoSalic":"D25"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_D25
> identificar_conhecimento_de_processo

## path2.24.oqueeh_estadoSalic{"estadoSalic":"D27"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_D27
> identificar_conhecimento_de_processo

## path2.25.oqueeh_estadoSalic{"estadoSalic":"E25"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E25
> identificar_conhecimento_de_processo

## path2.26.oqueeh_estadoSalic{"estadoSalic":"E62"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E62
> identificar_conhecimento_de_processo

## path2.27.oqueeh_estadoSalic{"estadoSalic":"E66"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E66
> identificar_conhecimento_de_processo

## path2.28.oqueeh_estadoSalic{"estadoSalic":"E20"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E20
> identificar_conhecimento_de_processo

## path2.29.oqueeh_estadoSalic{"estadoSalic":"E27"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E27
> identificar_conhecimento_de_processo

## path2.30.oqueeh_estadoSalic{"estadoSalic":"E30"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E30
> identificar_conhecimento_de_processo

## path2.31.oqueeh_estadoSalic{"estadoSalic":"E68"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E68
> identificar_conhecimento_de_processo

## path2.32.oqueeh_estadoSalic{"estadoSalic":"E77"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E77
> identificar_conhecimento_de_processo

## path2.33.oqueeh_estadoSalic{"estadoSalic":"L03"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_L03
> identificar_conhecimento_de_processo

## path2.34.oqueeh_estadoSalic{"estadoSalic":"L05"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_L05
> identificar_conhecimento_de_processo

## path2.35.oqueeh_estadoSalic{"estadoSalic":"L08"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_L08
> identificar_conhecimento_de_processo

## path2.36.oqueeh_estadoSalic{"estadoSalic":"L10"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_L10
> identificar_conhecimento_de_processo

## path2.37.oqueeh_estadoSalic{"estadoSalic":"L11"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_L11
> identificar_conhecimento_de_processo

## path2.38.oqueeh_estadoSalic{"estadoSalic":"D22"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_D22
> identificar_conhecimento_de_processo

## path2.39.oqueeh_estadoSalic{"estadoSalic":"D28"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_D28
> identificar_conhecimento_de_processo

## path2.40.oqueeh_estadoSalic{"estadoSalic":"E10"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E10
> identificar_conhecimento_de_processo

## path2.41.oqueeh_estadoSalic{"estadoSalic":"E11"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E11
> identificar_conhecimento_de_processo

## path2.42.oqueeh_estadoSalic{"estadoSalic":"E12"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E12
> identificar_conhecimento_de_processo

## path2.43.oqueeh_estadoSalic{"estadoSalic":"E13"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E13
> identificar_conhecimento_de_processo

## path2.44.oqueeh_estadoSalic{"estadoSalic":"E15"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E15
> identificar_conhecimento_de_processo

## path2.45.oqueeh_estadoSalic{"estadoSalic":"E16"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E16
> identificar_conhecimento_de_processo

## path2.46.oqueeh_estadoSalic{"estadoSalic":"E23"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E23
> identificar_conhecimento_de_processo

## path2.47.oqueeh_estadoSalic{"estadoSalic":"E24"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E24
> identificar_conhecimento_de_processo

## path2.48.oqueeh_estadoSalic{"estadoSalic":"E36"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E36
> identificar_conhecimento_de_processo

## path2.49.oqueeh_estadoSalic{"estadoSalic":"E59"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E59
> identificar_conhecimento_de_processo

## path2.50.oqueeh_estadoSalic{"estadoSalic":"E63"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E63
> identificar_conhecimento_de_processo

## path2.51.oqueeh_estadoSalic{"estadoSalic":"E15"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E15
> identificar_conhecimento_de_processo

## path2.52.oqueeh_estadoSalic{"estadoSalic":"E65"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E65
> identificar_conhecimento_de_processo

## path2.53.oqueeh_estadoSalic{"estadoSalic":"E75"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E75
> identificar_conhecimento_de_processo

## path2.52.oqueeh_estadoSalic{"estadoSalic":"E79"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E79
> identificar_conhecimento_de_processo

## path2.53.oqueeh_estadoSalic{"estadoSalic":"E80"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E80
> identificar_conhecimento_de_processo

## path2.54.oqueeh_estadoSalic{"estadoSalic":"E81"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E81
> identificar_conhecimento_de_processo

## path2.55.oqueeh_estadoSalic{"estadoSalic":"E60"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E60
> identificar_conhecimento_de_processo

## path2.56.oqueeh_estadoSalic{"estadoSalic":"E72"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E72
> identificar_conhecimento_de_processo

## path2.57.oqueeh_estadoSalic{"estadoSalic":"E72"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E72
> identificar_conhecimento_de_processo

## path2.58.oqueeh_estadoSalic{"estadoSalic":"E50"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E50
> identificar_conhecimento_de_processo

## path2.59.oqueeh_estadoSalic{"estadoSalic":"L09"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_L09
> identificar_conhecimento_de_processo

## path2.60.oqueeh_estadoSalic{"estadoSalic":"D38"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_D38
> identificar_conhecimento_de_processo

## path2.61.oqueeh_estadoSalic{"estadoSalic":"E22"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E22
> identificar_conhecimento_de_processo

## path2.62.oqueeh_estadoSalic{"estadoSalic":"E73"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E73
> identificar_conhecimento_de_processo

## path2.63.oqueeh_estadoSalic{"estadoSalic":"E78"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E78
> identificar_conhecimento_de_processo

## path2.64.oqueeh_estadoSalic{"estadoSalic":"E47"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_E47
> identificar_conhecimento_de_processo

## path2.65.oqueeh_estadoSalic{"estadoSalic":"L06"}
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic_L06
> identificar_conhecimento_de_processo

## path2.66.oqueEhSalicRouana
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalicRouana
> identificar_conhecimento_de_processo

## path2.67.oqueEhSalicLeiRouanet
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalicLeiRouanet
> identificar_conhecimento_de_processo

## path2.68.oqueEhSalicMinc
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalicMinc
> identificar_conhecimento_de_processo

## path2.69.oqueEhSalicSefic
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalicSefic
> identificar_conhecimento_de_processo

## path2.70.oqueEhSalicProjeto
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalicProjeto
> identificar_conhecimento_de_processo

## path2.71.oqueEhSalicProposta
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalicProposta
> identificar_conhecimento_de_processo

## path2.72.oqueEhSalicProponente
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalicProponente
> identificar_conhecimento_de_processo

## path2.73.oqueEhSalicPreenchimento
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalicPreenchimento
> identificar_conhecimento_de_processo

## path2.74.oqueEhSalicAdmissibilidade
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalicAdmissibilidade
> identificar_conhecimento_de_processo

## path2.75.oqueEhSalicAprovacao
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalicAprovacao
> identificar_conhecimento_de_processo

## path2.76.oqueEhSalicExecucao
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalicExecucao
> identificar_conhecimento_de_processo

## path2.77.oqueEhSalicPrestacaoDeContas
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalicPrestacaoDeContas
> identificar_conhecimento_de_processo

## path2.78.oqueEhSalic
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalic
> identificar_conhecimento_de_processo

## path2.79.oqueEhSalicVinculada
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_oqueEhSalicVinculada
> identificar_conhecimento_de_processo

## path2.1.1
> identificar_nova_proposta
* afirmar
  - utter_introduzir_contexto_nova_proposta
> identificar_contexto

## path2.1.2
> identificar_nova_proposta
* negar
  - utter_duvida_execucao
> identificar_execucao




<!--- Fluxo de Execução --->

## path2.1.2.1-fim
> identificar_execucao
* afirmar
  - utter_introduzir_execucao
  - utter_despedir

## path2.1.2.2
> identificar_execucao
* negar
  - utter_introduzir_contexto_nao_execucao
> identificar_contexto

## path2.1.2.3.oqueeh_estadoSalic{"estadoSalic":"A12"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_A12
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.4.oqueeh_estadoSalic{"estadoSalic":"A14"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_A14
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.5.oqueeh_estadoSalic{"estadoSalic":"A20"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_A20
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.6.oqueeh_estadoSalic{"estadoSalic":"A23"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_A23
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.7.oqueeh_estadoSalic{"estadoSalic":"B01"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_B01
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.8.oqueeh_estadoSalic{"estadoSalic":"B14"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_B14
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.9.oqueeh_estadoSalic{"estadoSalic":"A13"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_A13
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.10.oqueeh_estadoSalic{"estadoSalic":"A16"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_A16
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.11.oqueeh_estadoSalic{"estadoSalic":"A17"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_A17
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.12.oqueeh_estadoSalic{"estadoSalic":"A42"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_A42
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.13.oqueeh_estadoSalic{"estadoSalic":"B11"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_B11
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.14.oqueeh_estadoSalic{"estadoSalic":"B20"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_B20
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.15.oqueeh_estadoSalic{"estadoSalic":"C09"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_C09
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.16.oqueeh_estadoSalic{"estadoSalic":"C10"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_C10
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.17.oqueeh_estadoSalic{"estadoSalic":"C20"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_C20
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.18.oqueeh_estadoSalic{"estadoSalic":"C26"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_C26
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.19.oqueeh_estadoSalic{"estadoSalic":"C30"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_C30
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.20.oqueeh_estadoSalic{"estadoSalic":"D03"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_D03
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.21.oqueeh_estadoSalic{"estadoSalic":"D14"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_D14
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.22.oqueeh_estadoSalic{"estadoSalic":"D20"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_D20
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.23.oqueeh_estadoSalic{"estadoSalic":"D25"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_D25
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.24.oqueeh_estadoSalic{"estadoSalic":"D27"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_D27
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.25.oqueeh_estadoSalic{"estadoSalic":"E25"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E25
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.26.oqueeh_estadoSalic{"estadoSalic":"E62"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E62
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.27.oqueeh_estadoSalic{"estadoSalic":"E66"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E66
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.28.oqueeh_estadoSalic{"estadoSalic":"E20"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E20
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.29.oqueeh_estadoSalic{"estadoSalic":"E27"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E27
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.30.oqueeh_estadoSalic{"estadoSalic":"E30"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E30
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.31.oqueeh_estadoSalic{"estadoSalic":"E68"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E68
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.32.oqueeh_estadoSalic{"estadoSalic":"E77"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E77
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.33.oqueeh_estadoSalic{"estadoSalic":"L03"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_L03
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.34.oqueeh_estadoSalic{"estadoSalic":"L05"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_L05
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.35.oqueeh_estadoSalic{"estadoSalic":"L08"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_L08
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.36.oqueeh_estadoSalic{"estadoSalic":"L10"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_L10
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.37.oqueeh_estadoSalic{"estadoSalic":"L11"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_L11
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.38.oqueeh_estadoSalic{"estadoSalic":"D22"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_D22
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.39.oqueeh_estadoSalic{"estadoSalic":"D28"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_D28
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.40.oqueeh_estadoSalic{"estadoSalic":"E10"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E10
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.41.oqueeh_estadoSalic{"estadoSalic":"E11"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E11
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.42.oqueeh_estadoSalic{"estadoSalic":"E12"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E12
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.43.oqueeh_estadoSalic{"estadoSalic":"E13"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E13
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.44.oqueeh_estadoSalic{"estadoSalic":"E15"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E15
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.45.oqueeh_estadoSalic{"estadoSalic":"E16"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E16
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.46.oqueeh_estadoSalic{"estadoSalic":"E23"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E23
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.47.oqueeh_estadoSalic{"estadoSalic":"E24"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E24
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.48.oqueeh_estadoSalic{"estadoSalic":"E36"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E36
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.49.oqueeh_estadoSalic{"estadoSalic":"E59"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E59
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.50.oqueeh_estadoSalic{"estadoSalic":"E63"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E63
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.51.oqueeh_estadoSalic{"estadoSalic":"E15"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E15
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.52.oqueeh_estadoSalic{"estadoSalic":"E65"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E65
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.53.oqueeh_estadoSalic{"estadoSalic":"E75"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E75
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.52.oqueeh_estadoSalic{"estadoSalic":"E79"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E79
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.53.oqueeh_estadoSalic{"estadoSalic":"E80"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E80
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.54.oqueeh_estadoSalic{"estadoSalic":"E81"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E81
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.55.oqueeh_estadoSalic{"estadoSalic":"E60"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E60
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.56.oqueeh_estadoSalic{"estadoSalic":"E72"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E72
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.57.oqueeh_estadoSalic{"estadoSalic":"E72"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E72
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.58.oqueeh_estadoSalic{"estadoSalic":"E50"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E50
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.59.oqueeh_estadoSalic{"estadoSalic":"L09"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_L09
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.60.oqueeh_estadoSalic{"estadoSalic":"D38"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_D38
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.61.oqueeh_estadoSalic{"estadoSalic":"E22"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E22
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.62.oqueeh_estadoSalic{"estadoSalic":"E73"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E73
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.63.oqueeh_estadoSalic{"estadoSalic":"E78"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E78
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.64.oqueeh_estadoSalic{"estadoSalic":"E47"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_E47
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.65.oqueeh_estadoSalic{"estadoSalic":"L06"}
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic_L06
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.66.oqueEhSalicRouana
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalicRouana
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.67.oqueEhSalicLeiRouanet
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalicLeiRouanet
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.68.oqueEhSalicMinc
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalicMinc
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.69.oqueEhSalicSefic
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalicSefic
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.70.oqueEhSalicProjeto
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalicProjeto
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.71.oqueEhSalicProposta
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalicProposta
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.72.oqueEhSalicProponente
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalicProponente
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.73.oqueEhSalicPreenchimento
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalicPreenchimento
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.74.oqueEhSalicAdmissibilidade
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalicAdmissibilidade
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.75.oqueEhSalicAprovacao
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalicAprovacao
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.76.oqueEhSalicExecucao
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalicExecucao
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.77.oqueEhSalicPrestacaoDeContas
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalicPrestacaoDeContas
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.78.oqueEhSalic
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.79.oqueEhSalicVinculada
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalicVinculada
  - utter_duvida_execucao
> identificar_execucao


<!--- Conhecimento do Processo --->

## path2.2.1
> identificar_conhecimento_de_processo
* afirmar
  - utter_cadastro_salic
> identificar_cadastro_salic

## path2.2.2
> identificar_conhecimento_de_processo
* negar
  - utter_submissao_de_projetos
  - utter_cadastro_salic
> identificar_cadastro_salic

## pathCadastroSalic.1
> identificar_cadastro_salic
* afirmar
  - utter_ja_eh_proponente
> identificar_eh_proponente

## pathCadastroSalic.2
> identificar_cadastro_salic
* negar
  - utter_cadastro_salic_video
> identificar_explicar_cadastro

## pathCadastroSalic.3.oqueeh_estadoSalic{"estadoSalic":"A12"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_A12
> identificar_explicar_cadastro

## pathCadastroSalic.3.1.oqueeh_estadoSalic{"estadoSalic":"A14"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_A14
> identificar_explicar_cadastro

## pathCadastroSalic.3.2.oqueeh_estadoSalic{"estadoSalic":"A20"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_A20
> identificar_explicar_cadastro

## pathCadastroSalic.3.3.oqueeh_estadoSalic{"estadoSalic":"A23"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_A23
> identificar_explicar_cadastro

## pathCadastroSalic.3.4.oqueeh_estadoSalic{"estadoSalic":"B01"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_B01
> identificar_explicar_cadastro

## pathCadastroSalic.3.5.oqueeh_estadoSalic{"estadoSalic":"B14"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_B14
> identificar_explicar_cadastro

## pathCadastroSalic.3.6.oqueeh_estadoSalic{"estadoSalic":"A13"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_A13
> identificar_explicar_cadastro

## pathCadastroSalic.3.7.oqueeh_estadoSalic{"estadoSalic":"A16"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_A16
> identificar_explicar_cadastro

## pathCadastroSalic.3.8.oqueeh_estadoSalic{"estadoSalic":"A17"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_A17
> identificar_explicar_cadastro

## pathCadastroSalic.3.9.oqueeh_estadoSalic{"estadoSalic":"A42"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_A42
> identificar_explicar_cadastro

## pathCadastroSalic.3.10.oqueeh_estadoSalic{"estadoSalic":"B11"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_B11
> identificar_explicar_cadastro

## pathCadastroSalic.3.11.oqueeh_estadoSalic{"estadoSalic":"B20"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_B20
> identificar_explicar_cadastro

## pathCadastroSalic.3.12.oqueeh_estadoSalic{"estadoSalic":"C09"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_C09
> identificar_explicar_cadastro

## pathCadastroSalic.3.13.oqueeh_estadoSalic{"estadoSalic":"C10"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_C10
> identificar_explicar_cadastro

## pathCadastroSalic.3.14.oqueeh_estadoSalic{"estadoSalic":"C20"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_C20
> identificar_explicar_cadastro

## pathCadastroSalic.3.15.oqueeh_estadoSalic{"estadoSalic":"C26"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_C26
> identificar_explicar_cadastro

## pathCadastroSalic.3.16.oqueeh_estadoSalic{"estadoSalic":"C30"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_C30
> identificar_explicar_cadastro

## pathCadastroSalic.3.17.oqueeh_estadoSalic{"estadoSalic":"D03"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_D03
> identificar_explicar_cadastro

## pathCadastroSalic.3.18.oqueeh_estadoSalic{"estadoSalic":"D14"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_D14
> identificar_explicar_cadastro

## pathCadastroSalic.3.19.oqueeh_estadoSalic{"estadoSalic":"D20"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_D20
> identificar_explicar_cadastro

## pathCadastroSalic.3.20.oqueeh_estadoSalic{"estadoSalic":"D25"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_D25
> identificar_explicar_cadastro

## pathCadastroSalic.3.21.oqueeh_estadoSalic{"estadoSalic":"D27"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_D27
> identificar_explicar_cadastro

## pathCadastroSalic.3.22.oqueeh_estadoSalic{"estadoSalic":"E25"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E25
> identificar_explicar_cadastro

## pathCadastroSalic.3.23.oqueeh_estadoSalic{"estadoSalic":"E62"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E62
> identificar_explicar_cadastro

## pathCadastroSalic.3.24.oqueeh_estadoSalic{"estadoSalic":"E66"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E66
> identificar_explicar_cadastro

## pathCadastroSalic.3.25.oqueeh_estadoSalic{"estadoSalic":"E20"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E20
> identificar_explicar_cadastro

## pathCadastroSalic.3.26.oqueeh_estadoSalic{"estadoSalic":"E27"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E27
> identificar_explicar_cadastro

## pathCadastroSalic.3.27.oqueeh_estadoSalic{"estadoSalic":"E30"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E30
> identificar_explicar_cadastro

## pathCadastroSalic.3.28.oqueeh_estadoSalic{"estadoSalic":"E68"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E68
> identificar_explicar_cadastro

## pathCadastroSalic.3.29.oqueeh_estadoSalic{"estadoSalic":"E77"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E77
> identificar_explicar_cadastro

## pathCadastroSalic.3.30.oqueeh_estadoSalic{"estadoSalic":"L03"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_L03
> identificar_explicar_cadastro

## pathCadastroSalic.3.31.oqueeh_estadoSalic{"estadoSalic":"L05"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_L05
> identificar_explicar_cadastro

## pathCadastroSalic.3.32.oqueeh_estadoSalic{"estadoSalic":"L08"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_L08
> identificar_explicar_cadastro

## pathCadastroSalic.3.33.oqueeh_estadoSalic{"estadoSalic":"L10"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_L10
> identificar_explicar_cadastro

## pathCadastroSalic.3.34.oqueeh_estadoSalic{"estadoSalic":"L11"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_L11
> identificar_explicar_cadastro

## pathCadastroSalic.3.35.oqueeh_estadoSalic{"estadoSalic":"D22"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_D22
> identificar_explicar_cadastro

## pathCadastroSalic.3.36.oqueeh_estadoSalic{"estadoSalic":"D28"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_D28
> identificar_explicar_cadastro

## pathCadastroSalic.3.37.oqueeh_estadoSalic{"estadoSalic":"E10"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E10
> identificar_explicar_cadastro

## pathCadastroSalic.3.38.oqueeh_estadoSalic{"estadoSalic":"E11"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E11
> identificar_explicar_cadastro

## pathCadastroSalic.3.39.oqueeh_estadoSalic{"estadoSalic":"E12"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E12
> identificar_explicar_cadastro

## pathCadastroSalic.3.40.oqueeh_estadoSalic{"estadoSalic":"E13"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E13
> identificar_explicar_cadastro

## pathCadastroSalic.3.41.oqueeh_estadoSalic{"estadoSalic":"E15"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E15
> identificar_explicar_cadastro

## pathCadastroSalic.3.42.oqueeh_estadoSalic{"estadoSalic":"E16"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E16
> identificar_explicar_cadastro

## pathCadastroSalic.3.43.oqueeh_estadoSalic{"estadoSalic":"E23"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E23
> identificar_explicar_cadastro

## pathCadastroSalic.3.43.oqueeh_estadoSalic{"estadoSalic":"E24"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E24
> identificar_explicar_cadastro

## pathCadastroSalic.3.44.oqueeh_estadoSalic{"estadoSalic":"E36"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E36
> identificar_explicar_cadastro

## pathCadastroSalic.3.45.oqueeh_estadoSalic{"estadoSalic":"E59"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E59
> identificar_explicar_cadastro

## pathCadastroSalic.3.46.oqueeh_estadoSalic{"estadoSalic":"E63"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E63
> identificar_explicar_cadastro

## pathCadastroSalic.3.47.oqueeh_estadoSalic{"estadoSalic":"E15"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E15
> identificar_explicar_cadastro

## pathCadastroSalic.3.48.oqueeh_estadoSalic{"estadoSalic":"E65"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E65
> identificar_explicar_cadastro

## pathCadastroSalic.3.49.oqueeh_estadoSalic{"estadoSalic":"E75"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E75
> identificar_explicar_cadastro

## pathCadastroSalic.3.50.oqueeh_estadoSalic{"estadoSalic":"E79"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E79
> identificar_explicar_cadastro

## pathCadastroSalic.3.51.oqueeh_estadoSalic{"estadoSalic":"E80"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E80
> identificar_explicar_cadastro

## pathCadastroSalic.3.52.oqueeh_estadoSalic{"estadoSalic":"E81"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E81
> identificar_explicar_cadastro

## pathCadastroSalic.3.53.oqueeh_estadoSalic{"estadoSalic":"E60"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E60
> identificar_explicar_cadastro

## pathCadastroSalic.3.54.oqueeh_estadoSalic{"estadoSalic":"E72"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E72
> identificar_explicar_cadastro

## pathCadastroSalic.3.55.oqueeh_estadoSalic{"estadoSalic":"E72"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E72
> identificar_explicar_cadastro

## pathCadastroSalic.3.56.oqueeh_estadoSalic{"estadoSalic":"E50"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E50
> identificar_explicar_cadastro

## pathCadastroSalic.3.57.oqueeh_estadoSalic{"estadoSalic":"L09"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_L09
> identificar_explicar_cadastro

## pathCadastroSalic.3.58.oqueeh_estadoSalic{"estadoSalic":"D38"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_D38
> identificar_explicar_cadastro

## pathCadastroSalic.3.59.oqueeh_estadoSalic{"estadoSalic":"E22"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E22
> identificar_explicar_cadastro

## pathCadastroSalic.3.60.oqueeh_estadoSalic{"estadoSalic":"E73"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E73
> identificar_explicar_cadastro

## pathCadastroSalic.3.61.oqueeh_estadoSalic{"estadoSalic":"E78"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E78
> identificar_explicar_cadastro

## pathCadastroSalic.3.62.oqueeh_estadoSalic{"estadoSalic":"E47"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_E47
> identificar_explicar_cadastro

## pathCadastroSalic.3.63.oqueeh_estadoSalic{"estadoSalic":"L06"}
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalic_L06
> identificar_explicar_cadastro

## pathCadastroSalic.3.64.oqueEhSalicRouana
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalicRouana
> identificar_explicar_cadastro

## pathCadastroSalic.3.65.oqueEhSalicLeiRouanet
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalicLeiRouanet
> identificar_explicar_cadastro

## pathCadastroSalic.3.66.oqueEhSalicMinc
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalicMinc
> identificar_explicar_cadastro

## pathCadastroSalic.3.67.oqueEhSalicSefic
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalicSefic
> identificar_explicar_cadastro

## pathCadastroSalic.3.68.oqueEhSalicProjeto
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalicProjeto
> identificar_explicar_cadastro

## pathCadastroSalic.3.69.oqueEhSalicProposta
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalicProposta
> identificar_explicar_cadastro

## pathCadastroSalic.3.70.oqueEhSalicProponente
> identificar_cadastro_salic
* o_que_eh
  - utter_oqueEhSalicProponente
> identificar_explicar_cadastro

## path2.1.2.73.oqueEhSalicPreenchimento
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalicPreenchimento
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.74.oqueEhSalicAdmissibilidade
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalicAdmissibilidade
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.75.oqueEhSalicAprovacao
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalicAprovacao
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.76.oqueEhSalicExecucao
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalicExecucao
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.77.oqueEhSalicPrestacaoDeContas
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalicPrestacaoDeContas
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.78.oqueEhSalic
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalic
  - utter_duvida_execucao
> identificar_execucao

## path2.1.2.79.oqueEhSalicVinculada
> identificar_execucao
* o_que_eh
  - utter_oqueEhSalicVinculada
  - utter_duvida_execucao
> identificar_execucao

## pathCadastroSalic.2.1
> identificar_explicar_cadastro
* afirmar
  - utter_explicar_cadastro_salic
  - utter_ja_eh_proponente
> identificar_eh_proponente


## pathCadastroSalic.2.2
> identificar_explicar_cadastro
* negar
  - utter_cadastro_salic_apos_video
  - utter_inscricao_proponente
  - utter_cadastro_proponente_introduzir_contexto
> identificar_contexto

## pathCadastroProponente.1
> identificar_eh_proponente
* afirmar
  - utter_cadastro_proponente_introduzir_contexto
> identificar_contexto

## pathCadastroProponente.2
> identificar_eh_proponente
* negar
  - utter_inscricao_proponente
  - utter_cadastro_proponente_introduzir_contexto
> identificar_contexto

## pathCadastroProponente.3
> identificar_eh_proponente
* o_que_eh
  - utter_o_que_eh
  - utter_cadastro_proponente_introduzir_contexto
> identificar_contexto



<!--- Contexto --->


## pathContexto.processo
> identificar_contexto
  - utter_definir_contexto
* escolher_processo
  - utter_explicar_processo
  - utter_ainda_nao_aprendi
  - utter_despedir
  - utter_restart

## pathContexto.preenchimento
> identificar_contexto
  - utter_definir_contexto
* escolher_preenchimento
  - utter_explicar_preenchimento
  - utter_ainda_nao_aprendi
  - utter_despedir
  - utter_restart

## pathContexto.prazo
> identificar_contexto
  - utter_definir_contexto
* escolher_prazo
  - utter_explicar_prazo
  - utter_ainda_nao_aprendi
  - utter_despedir
  - utter_restart

## pathContexto.errossalic
> identificar_contexto
  - utter_definir_contexto
* escolher_erros_salic
  - utter_explicar_erros_salic
  - utter_ainda_nao_aprendi
  - utter_despedir
  - utter_restart

## pathContexto.5
> identificar_contexto
  - utter_definir_contexto
* duvida_sobre_contexto OR negar
  - utter_explicar_contextos
> identificar_contexto

## pathContexto.oqueeh
> identificar_contexto
  - utter_definir_contexto
* o_que_eh
  - utter_o_que_eh
> identifica_mais_alguma_pergunta

## pathMaisPergunta.1
> identifica_mais_alguma_pergunta
  - utter_mais_alguma_pergunta
* afirmar
  - utter_mais_perguntas_afirmativa
> identificar_contexto

## pathMaisPergunta.2-fim
> identifica_mais_alguma_pergunta
  - utter_mais_alguma_pergunta
* negar
  - utter_despedir
  - utter_restart
