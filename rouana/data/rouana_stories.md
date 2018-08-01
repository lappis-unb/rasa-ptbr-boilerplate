## path
* cumprimentar
  - utter_cumprimetar
  - utter_definir_perfil
> identifica_perfil

<!--- Fluxos Curiosidades --->

## path1
> identifica_perfil
* afirmar_curiosidades
  - ActionIndicacaoCuriosidades
> identificar_curiosidade

## path1.1
> identificar_curiosidade
*  lei_rouanet_definicao
  - ActionDefinicaoLei

## path1.2
> identificar_curiosidade
* lei_rouanet_quantidade_projetos
  - ActionQuantidadeProjetos

## path1.3
> identificar_curiosidade
* lei_rouanet_arrecadacao
  - ActionArrecadacaoLei

## path1.4
> identificar_curiosidade
* submissao_de_projeto
  - ActionSubmissaoDeProjetos

<!--- Fluxos Propostas e Projetos --->

## path2
> identifica_perfil
* afirmar_projeto
  - ActionAviso
> identificar_preenchimento_de_proposta

## path2.1
> identificar_preenchimento_de_proposta
* afirmar_preencheu_proposta
  - utter_nova_proposta
> identificar_nova_proposta

## path2.1.1
> identificar_nova_proposta
* afirmar_nova_proposta
> identificar_contexto

## path2.1.2
> identificar_nova_proposta
* negar_nova_proposta
  - utter_duvida_execucao
> identificar_execucao

<!--- TODO - FLUXO DE EXECUÇÂO --->
## path2.1.2.1
> identificar_execucao
* afirmar_execucao
  - ActionIntroduzirExecucao

## path2.1.2.2
> identificar_execucao
* negar_execucao
> identificar_contexto

<!--- TODO - FLUXO DE EXECUÇÂO --->

## path2.2
> identificar_preenchimento_de_proposta
* negar_preencheu_proposta
  - utter_conhece_processo
> identificar_conhecimento_de_processo

<!--- Conhecimento do Processo --->

## path2.2.1
> identificar_conhecimento_de_processo
* afirmar_conhecimento_processo

## path2.2.2
> identificar_conhecimento_de_processo
* negar_conhecimento_processo
  - ActionSubmissaoDeProjetos
> especificar_processo

<!--- Conhecimento do Processo --->

<!---TODO - FLUXO EXPLICAÇÃO DO PROCESSO --->

## path2.2.2.1
> especificar_processo
* afirmar_especificar_processo
  - utter_especificar_processo

## path2.2.2.1
> especificar_processo
* negar_especificar_processo
  - utter_cadastro_salic


<!---TODO - FLUXO EXPLICAÇÃO DO PROCESSO --->





<!--- Fluxo de Conhecimento do Processo --->


## pathContexto
> identificar_contexto
- ActionDefinirContexto

# pathCadastroSalic
> idenficar_cadastro_no_salic
