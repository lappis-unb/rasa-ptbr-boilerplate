import re
import spacy

from rasa_core.actions.action import Action
from rasa_core.events import UserUtteranceReverted


class ActionMultiline(Action):
    messages = ['']

    def name(self):
        return self.convert_name_to_snake_case()

    def run(self, dispatcher, tracker, domain):
        for message in self.messages:
            dispatcher.utter_message(message)
        return []

    def convert_name_to_snake_case(self):
        return re.sub('(.)([A-Z]{1})', r'\1_\2',
                      self.__class__.__name__).lower()


class ActionRevert(Action):
    def name(self):
        return "action_revert"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Sorry, didn't get that. Try again.")
        return [UserUtteranceReverted()]
