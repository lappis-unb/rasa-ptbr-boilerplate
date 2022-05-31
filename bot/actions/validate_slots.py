from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ValidateConsultaForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_consulta_form"

    def validate_tipo_consulta(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate tipo_consulta"""

        tipo_consulta = slot_value

        if tipo_consulta.isdigit():
            tipo_consulta = int(tipo_consulta)
            if tipo_consulta > 0 and tipo_consulta <= 3:
                # validation succeeded
                return {"tipo_consulta": tipo_consulta}
        # validation failed
        dispatcher.utter_message(response="utter_tipo_consulta_errado")
        return {"tipo_consulta": None}

        #if slot_value.lower() in self.cuisine_db():
        #    # validation succeeded, set the value of the "cuisine" slot to value
        #    return {"cuisine": slot_value}
        #else:
        #    # validation failed, set this slot to None so that the
        #    # user will be asked for the slot again
        #    return {"cuisine": None}
