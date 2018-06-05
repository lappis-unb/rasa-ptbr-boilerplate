## primeira_interacao
* cumprimento
- action_apresentacao_basica
- action_pergunta_de_perfil
* resposta_positiva
  - action_confirma_proponente
  - slot{"eh_proponente": "true"}
  - action_resposta_positiva
- action_responder

## primeira_interacao
* cumprimento
- action_apresentacao_basica
- action_pergunta_de_perfil
* resposta_negativa
  - action_desconfirma_proponente
  - slot{"eh_proponente": "false"}
  - action_resposta_negativa
- action_responder

