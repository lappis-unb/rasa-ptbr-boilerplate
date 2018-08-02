## path
* cumprimentar
  - ActionCumprimentar
  - ActionDefinirPerfil
> identifica_perfil




<!--- Fluxo Curiosidades --->

## path1
> identifica_perfil
* afirmar_curiosidades
  - ActionCuriosidadesIndicacao
> identificar_curiosidade

## path1.end.1
> curiosidade_final
* afirmar
  - ActionCuriosidadesMaisSim
> identificar_curiosidade

## path1.end.2
> curiosidade_final
* negar
  - ActionCuriosidadesMaisNao
> curiosidade_falar_sobre_projetos

## path1.end.2.1
> curiosidade_falar_sobre_projetos
* afirmar
  - ActionCuriosidadesFalarSobreProjetos
  - ActionAviso
> identificar_preenchimento_de_proposta

## path1.end.2.2-fim
> curiosidade_falar_sobre_projetos
* negar
  - ActionCuriosidadesFim




<!--- Fluxos Propostas e Projetos --->

## path2
> identifica_perfil
* afirmar_projeto
  - ActionAviso
> identificar_preenchimento_de_proposta

## path2.1
> identificar_preenchimento_de_proposta
* afirmar_preencheu_proposta
  - ActionNovaProposta
> identificar_nova_proposta

## path2.1.1
> identificar_nova_proposta
* afirmar_nova_proposta
> identificar_contexto

## path2.1.2
> identificar_nova_proposta
* negar
  - ActionDuvidaExecucao
> identificar_execucao




<!--- Fluxo de Execução --->

## path2.1.2.1-fim
> identificar_execucao
* afirmar_execucao
  - ActionIntroduzirExecucao

## path2.1.2.2
> identificar_execucao
* negar
> identificar_contexto

<!--- TODO - FLUXO DE EXECUÇÂO --->




## path2.2
> identificar_preenchimento_de_proposta
* negar
  - ActionConheceProcesso
> identificar_conhecimento_de_processo

<!--- Conhecimento do Processo --->

## path2.2.1
> identificar_conhecimento_de_processo
* afirmar_conhecimento_processo

## path2.2.2
> identificar_conhecimento_de_processo
* negar
  - ActionSubmissaoDeProjetos
> especificar_processo

<!--- Conhecimento do Processo --->

<!---TODO - FLUXO EXPLICAÇÃO DO PROCESSO --->

## path2.2.2.1
> especificar_processo
* afirmar
  - ActionEspecificarProcesso

## path2.2.2.1
> especificar_processo
* negar
  - ActionCadastroSalic


<!---TODO - FLUXO EXPLICAÇÃO DO PROCESSO --->





<!--- Fluxo de Conhecimento do Processo --->

## pathContexto
> identificar_contexto
- ActionDefinirContexto

# pathCadastroSalic
> idenficar_cadastro_no_salic
