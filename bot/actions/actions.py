# Este arquivo contém custom actions que utilizão código python
# para executar ações no diálogo.
#
# Veja o guia na documentação do RASA em:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionTeste(Action):
    def name(self) -> Text:
        return "action_teste"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        try:
            dispatcher.utter_message("Mensagem enviada por uma custom action.")
        except ValueError:
            dispatcher.utter_message(ValueError)
        return []


class ActionTelefone(Action):
    def name(self) -> Text:
        return "action_telefone"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        telefone = tracker.get_slot('telefone')

        try:
            dispatcher.utter_message("O seu telefone é {}?".format(telefone))
        except ValueError:
            dispatcher.utter_message(ValueError)
        return [SlotSet("telefone", telefone)]
