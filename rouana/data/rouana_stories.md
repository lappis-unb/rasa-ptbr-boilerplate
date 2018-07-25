## path1
* cumprimentar
  - utter_cumprimetar
  - utter_perguntar_eh_proponete
> check_asked_question


## path11
> check_asked_question
* afirmar_proponente
  - action_set_slot_true
  - utter_despedir

## path12
> check_asked_question
* negar_proponente
  - action_set_slot_false
  - utter_despedir

## path13
> check_asked_question
* o_que_eh
  - action_what_is
  - utter_despedir

