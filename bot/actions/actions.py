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

        self.send_message(dispatcher, tracker, text)
        self.get_message_tracker(dispatcher, tracker, text)

    def send_message(self, dispatcher, tracker, text):
        payload = {'query': text}
        payload = json.dumps(payload)
        header = {"content-type": "application/json"}

        r = requests.post("http://tais:5005/conversations/default/respond",
                          data=payload, headers=header)

        for i in range(0, len(r.json())):
            dispatcher.utter_message(r.json()[i]['text'])

    def get_message_tracker(self, dispatcher, tracker, text):
        payload = {'query': text}
        payload = json.dumps(payload)
        header = {"content-type": "application/json"}

        r = requests.get("http://tais:5005/conversations/default/tracker",
                         data=payload, headers=header)
        r = r.json()
        for event in r['events']:
            if 'parse_data' in event:
                logger.warning(event['text'])
                logger.warning(event['parse_data']['intent']['confidence'])
