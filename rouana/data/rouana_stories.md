<!--- Fluxos Curiosidades --->

## path1
* cumprimentar
  - utter_cumprimetar
  - utter_definir_perfil
* afirmar_curiosidades
  - action_indicacao_curiosidades
> identificar_curiosidade

## path1.1
> identificar_curiosidade
*  lei_rouanet_definicao
  - action_definicao_lei

## path1.2
> identificar_curiosidade
* lei_rouanet_quantidade_projetos
  - action_quantidade_projetos

## path1.3
> identificar_curiosidade
* lei_rouanet_arrecadacao
  - action_arrecadacao_lei

## path1.4
> identificar_curiosidade
* submissao_de_projeto 
  - action_submissao_de_projeto

<!--- Fluxos Propostas e Projetos --->

## path2
* cumprimentar
  - utter_cumprimetar
  - utter_definir_perfil
* afirmar_projeto
  - action_aviso
> identificar_preenchimento_de_proposta

## path2.1
> identificar_preenchimento_de_proposta
* afirmar_preencheu_proposta
  - utter_nova_proposta
> identificar_nova_proposta

## path2.1.1
> identificar_nova_proposta
* afirmar_nova_proposta

## path2.1.2
> identificar_nova_proposta
* negar_nova_proposta

## path2.2
> identificar_preenchimento_de_proposta
* negar_preencheu_proposta

