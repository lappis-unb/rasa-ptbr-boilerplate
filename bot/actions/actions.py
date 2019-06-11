from rasa_core_sdk import Action
import requests
import json
import logging

logger = logging.getLogger(__name__)


class ActionTest(Action):
    def name(self):
        return "action_test"

    def run(self, dispatcher, tracker, domain):
        try:
            dispatcher.utter_message("Mensagem enviada por uma custom action.")
        except ValueError:
            dispatcher.utter_message(ValueError)


class ActionFallback(Action):
    def name(self):
        return "action_fallback"

    def run(self, dispatcher, tracker, domain):
        text = ''
        text = tracker.latest_message.get('text')
        r = ''
        payload = {'query': text}
        payload = json.dumps(payload)
        header = {"content-type": "application/json"}

        r = requests.post("http://tais:5005/conversations/default/respond",
                          data=payload, headers=header)
        logger.warning(str(r.text))
        r = r.text
        # logger.warning("************************" + r[0] + "*********************************")
        r = json.loads(r)
        # logger.warning("teste " + r["text"])
        dispatcher.utter_message("ola")
