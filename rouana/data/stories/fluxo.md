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

## path2.3
> identificar_preenchimento_de_proposta
* o_que_eh
  - utter_o_que_eh
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

## path2.1.2.3
> identificar_execucao
* o_que_eh
  - utter_o_que_eh
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

## pathCadastroSalic.3
> identificar_cadastro_salic
* o_que_eh
  - utter_o_que_eh
> identificar_explicar_cadastro

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
