from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

class ActionConfirmaProponente(Action):
    def name(self):
        return 'action_confirma_proponente'

    def run(self, dispatcher, tracker, domain):
        # dispatcher.utter_message("genericao: yaya")
        return [SlotSet("eh_proponente", "true")]

class ActionDesconfirmaProponente(Action):
    def name(self):
        return 'action_desconfirma_proponente'

    def run(self, dispatcher, tracker, domain):
        # dispatcher.utter_message("genericao: yaya")
        return [SlotSet("eh_proponente", "false")]

