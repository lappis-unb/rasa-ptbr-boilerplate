## path
* cumprimentar
  - action_cumprimentar
  - action_definir_perfil
> identifica_perfil




<!--- Fluxo Curiosidades --->

## path1
> identifica_perfil
* afirmar_curiosidades
  - action_curiosidades_indicacao
> identificar_curiosidade

## path1.end.1
> curiosidade_final
* afirmar
  - action_curiosidades_mais_sim
> identificar_curiosidade

## path1.end.2
> curiosidade_final
* negar
  - action_curiosidades_mais_nao
> curiosidade_falar_sobre_projetos

## path1.end.2.1
> curiosidade_falar_sobre_projetos
* afirmar
  - action_curiosidades_falar_sobre_projetos
  - action_aviso
> identificar_preenchimento_de_proposta

## path1.end.2.2-fim
> curiosidade_falar_sobre_projetos
* negar
  - action_curiosidades_fim




<!--- Fluxos Propostas e Projetos --->

## path2
> identifica_perfil
* afirmar_projeto
  - action_aviso
> identificar_preenchimento_de_proposta

## path2.1
> identificar_preenchimento_de_proposta
* afirmar_preencheu_proposta
  - action_nova_proposta
> identificar_nova_proposta

## path2.1.1
> identificar_nova_proposta
* afirmar_nova_proposta
> identificar_contexto

## path2.1.2
> identificar_nova_proposta
* negar
  - action_duvida_execucao
> identificar_execucao




<!--- Fluxo de Execução --->

## path2.1.2.1-fim
> identificar_execucao
* afirmar_execucao
  - action_introduzir_execucao

## path2.1.2.2
> identificar_execucao
* negar
> identificar_contexto

<!--- TODO - FLUXO DE EXECUÇÂO --->




## path2.2
> identificar_preenchimento_de_proposta
* negar
  - action_conhece_processo
> identificar_conhecimento_de_processo

<!--- Conhecimento do Processo --->

## path2.2.1
> identificar_conhecimento_de_processo
* afirmar_conhecimento_processo

## path2.2.2
> identificar_conhecimento_de_processo
* negar
  - action_submissao_de_projetos
> especificar_processo

<!--- Conhecimento do Processo --->

<!---TODO - FLUXO EXPLICAÇÃO DO PROCESSO --->

## path2.2.2.1
> especificar_processo
* afirmar
  - action_especificar_processo

## path2.2.2.1
> especificar_processo
* negar
  - action_cadastro_salic


<!---TODO - FLUXO EXPLICAÇÃO DO PROCESSO --->





<!--- Fluxo de Conhecimento do Processo --->

## pathContexto
> identificar_contexto
- action_definir_contexto

# pathCadastroSalic
> idenficar_cadastro_no_salic
