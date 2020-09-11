# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any, Text, Dict, List, Union
import re

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction

from .data_validator import isCpfValid


class LoginForm(FormAction):
    """Form used to handle login information"""

    def name(self) -> Text:
        """Unique identifier of the form"""
        return "login_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that will be needed to login"""
        return ["cpf", "data_nascimento"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        return {
            "cpf": self.from_text(not_intent="cancelar"),
            "data_nascimento": self.from_text(not_intent="cancelar"),
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the login form will do after
            all required slots are filled"""

        cpf = tracker.get_slot("cpf")
        data_nascimento = tracker.get_slot("data_nascimento")
        dispatcher.utter_message(
            "Então seu CPF é: {} e sua data de nascimento é: {}?".format(
                cpf, data_nascimento
            )
        )
        return []

    def validate_cpf(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate cpf value."""

        regex = re.compile("[0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2}$")
        if re.match(regex, value) is None:
            dispatcher.utter_template("utter_errado_cpf_formato", tracker)
            return {"cpf": None}
        elif not isCpfValid(value):
            dispatcher.utter_template("utter_errado_cpf_invalido", tracker)
            return {"cpf": None}
        else:
            return {"cpf": value}

    def validate_data_nascimento(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate data_nascimento value."""

        regex = re.compile(
            "(([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4})"
        )
        if re.match(regex, value) is not None:
            return {"data_nascimento": value}
        else:
            dispatcher.utter_template("utter_errado_data_nascimento", tracker)
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"data_nascimento": None}

