## path0.1
* negar
  - action_fase_de_testes
  - action_definir_perfil
> identifica_perfil

## path0.2
* afirmar
  - action_definir_perfil
> identifica_perfil


<!--- Fluxo Curiosidades --->

## path1-negar
> identifica_perfil
* negar
  - action_explicar_definicao_perfil
> identifica_perfil

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
  - action_despedir
  - action_restart



<!--- Fluxos Propostas e Projetos --->

## path2
> identifica_perfil
* afirmar_projeto
  - action_aviso
> identificar_preenchimento_de_proposta

## path2.1
> identificar_preenchimento_de_proposta
* afirmar
  - action_nova_proposta
> identificar_nova_proposta

## path2.2
> identificar_preenchimento_de_proposta
* negar
  - action_conhece_processo
> identificar_conhecimento_de_processo

## path2.3
> identificar_preenchimento_de_proposta
* o_que_eh
  - action_o_que_eh
> identificar_conhecimento_de_processo

## path2.1.1
> identificar_nova_proposta
* afirmar
  - action_introduzir_contexto_nova_proposta
> identificar_contexto

## path2.1.2
> identificar_nova_proposta
* negar
  - action_duvida_execucao
> identificar_execucao




<!--- Fluxo de Execução --->

## path2.1.2.1-mais_alguma_pergunta
> identificar_execucao
* afirmar
  - action_introduzir_execucao
> identifica_mais_alguma_pergunta

## path2.1.2.2
> identificar_execucao
* negar
  - action_introduzir_contexto_nao_execucao
> identificar_contexto

## path2.1.2.3
> identificar_execucao
* o_que_eh
  - action_o_que_eh
  - action_duvida_execucao
> identificar_execucao



<!--- Conhecimento do Processo --->

## path2.2.1
> identificar_conhecimento_de_processo
* afirmar
  - action_cadastro_salic
> identificar_cadastro_salic

## path2.2.2
> identificar_conhecimento_de_processo
* negar
  - action_submissao_de_projetos
  - action_cadastro_salic
> identificar_cadastro_salic

## pathCadastroSalic.1
> identificar_cadastro_salic
* afirmar
  - action_ja_eh_proponente
> identificar_eh_proponente

## pathCadastroSalic.2
> identificar_cadastro_salic
* negar
  - action_cadastro_salic_video
> identificar_explicar_cadastro

## pathCadastroSalic.3
> identificar_cadastro_salic
* o_que_eh
  - action_o_que_eh
> identificar_explicar_cadastro

## pathCadastroSalic.2.1
> identificar_explicar_cadastro
* afirmar
  - action_explicar_cadastro_salic
  - action_ja_eh_proponente
> identificar_eh_proponente


## pathCadastroSalic.2.2
> identificar_explicar_cadastro
* negar
  - action_cadastro_salic_apos_video
  - action_inscricao_proponente
  - action_cadastro_proponente_introduzir_contexto
> identificar_contexto

## pathCadastroProponente.1
> identificar_eh_proponente
* afirmar
  - action_cadastro_proponente_introduzir_contexto
> identificar_contexto

## pathCadastroProponente.2
> identificar_eh_proponente
* negar
  - action_inscricao_proponente
  - action_cadastro_proponente_introduzir_contexto
> identificar_contexto

## pathCadastroProponente.3
> identificar_eh_proponente
* o_que_eh
  - action_o_que_eh
  - action_cadastro_proponente_introduzir_contexto
> identificar_contexto



<!--- Contexto --->


## pathContexto.processo
> identificar_contexto
  - action_definir_contexto
* escolher_processo
  - action_explicar_processo
  - action_ainda_nao_aprendi
> identifica_mais_alguma_pergunta

## pathContexto.preenchimento
> identificar_contexto
  - action_definir_contexto
* escolher_preenchimento
  - action_explicar_preenchimento
  - action_ainda_nao_aprendi
> identifica_mais_alguma_pergunta

## pathContexto.prazo
> identificar_contexto
  - action_definir_contexto
* escolher_prazo
  - action_explicar_prazo
  - action_ainda_nao_aprendi
> identifica_mais_alguma_pergunta

## pathContexto.errossalic
> identificar_contexto
  - action_definir_contexto
* escolher_erros_salic
  - action_explicar_erros_salic
  - action_ainda_nao_aprendi
> identifica_mais_alguma_pergunta

## pathContexto.5
> identificar_contexto
  - action_definir_contexto
* duvida_sobre_contexto OR negar
  - action_explicar_contextos
> identificar_contexto

## pathContexto.oqueeh
> identificar_contexto
  - action_definir_contexto
* o_que_eh
  - action_o_que_eh
> identifica_mais_alguma_pergunta

## pathMaisPergunta.1
> identifica_mais_alguma_pergunta
  - action_mais_alguma_pergunta
* afirmar
> identificar_contexto

## pathMaisPergunta.2-fim
> identifica_mais_alguma_pergunta
  - action_mais_alguma_pergunta
* negar
  - action_curiosidades_mais
* afirmar
  - action_curiosidades_mais_sim
> identificar_curiosidade

## pathMaisPergunta.3-fim
> identifica_mais_alguma_pergunta
  - action_mais_alguma_pergunta
* negar
  - action_curiosidades_mais
* negar
  - action_despedir
  - action_restart
