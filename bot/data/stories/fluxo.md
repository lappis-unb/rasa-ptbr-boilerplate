## path0.1
* negar
  - utter_fase_de_testes
  - utter_definir_perfil
> identifica_perfil

## path0.2
* afirmar
  - utter_definir_perfil
> identifica_perfil


<!--- Fluxo Curiosidades --->

## path1-negar
> identifica_perfil
* negar
  - utter_explicar_definicao_perfil
> identifica_perfil

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
  - action_o_que_eh
> identificar_conhecimento_de_processo

## path2.1.1
> identificar_nova_proposta
* afirmar
> identificar_contexto

## path2.1.2
> identificar_nova_proposta
* negar
  - utter_duvida_execucao
> identificar_execucao


<!--- Fluxo de Execução --->

## path2.1.2.1-mais_alguma_pergunta
> identificar_execucao
* afirmar
  - utter_introduzir_execucao
> mais_alguma_pergunta

## path2.1.2.2
> identificar_execucao
* negar
> identificar_contexto

## path2.1.2.3
> identificar_execucao
* o_que_eh
  - action_o_que_eh
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
  - action_o_que_eh
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
  - utter_proponente_cadastrado
> mais_alguma_pergunta

## pathCadastroProponente.1
> identificar_eh_proponente
* afirmar
  - utter_proponente_cadastrado
> mais_alguma_pergunta

## pathCadastroProponente.2
> identificar_eh_proponente
* negar
  - utter_inscricao_proponente
  - utter_proponente_cadastrado
> mais_alguma_pergunta

## pathCadastroProponente.3
> identificar_eh_proponente
* o_que_eh
  - action_o_que_eh
  - utter_proponente_cadastrado
> mais_alguma_pergunta



<!--- Contexto --->


## pathContexto
> identificar_contexto
  - utter_nao_aprendi_contexto
> mais_alguma_pergunta


## pathMaisPergunta.2
> mais_alguma_pergunta
  - utter_mais_alguma_pergunta
* negar
  - utter_curiosidades_mais
* afirmar
  - utter_curiosidades_mais_sim
> identificar_curiosidade

## pathMaisPergunta.3-fim
> mais_alguma_pergunta
  - utter_mais_alguma_pergunta
* negar
  - utter_curiosidades_mais
* negar
  - utter_despedir
  - utter_restart

## pathMaisPergunta.4-fim
> mais_alguma_pergunta
  - utter_mais_alguma_pergunta
* afirmar
> oque_eh

## pathMaisPergunta.5-fim
> oque_eh
- utter_curiosidades_mais_sim
* o_que_eh
  - action_o_que_eh
> mais_alguma_pergunta

## fallback
- action_default_fallback
