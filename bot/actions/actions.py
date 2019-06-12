from rasa_core_sdk import Action
import json
import logging
from .api_helper import get_request, post_request

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

        bots = ["tais:5005"]

        answers = self.ask_bots(text, bots)

        answer = self.get_best_answer(answers)
        
        logger.debug("Remote Utter: " + answer.info.utter)
        logger.debug("Remote Intent: " + answer.info.intent)
        logger.debug("Remote Confidence: " + answer.confidence)
        
        for message in answer.messages:
            dispatcher.utter_message(message)


    def get_best_answer(self, answers):
        max_confidence = max([answer['confidence'] for answer in answers])
        best_answer = {}
        for answer in answers:
            if(answer.confidence >= max_confidence):
                best_answer = answer
        return best_answer


    def ask_bots(self, text, bots):
        answers = []
        for bot in bots:
            messages = self.send_message(text, bot)
            info = self.get_message_info(text, bot)
            bot_answer = {
                "messages": messages,
                "info": info,
                "confidence": info.confidence
            }
            answers.append(bot_answer)

        return answers


    def send_message(self, text, bot_url):
        payload = {'query': text}
        payload = json.dumps(payload)

        r = post_request(payload, "http://" + bot_url + "/conversations/default/respond")
        messages = []
        for i in range(0, len(r)):
            messages.append(r[i]['text'])
        return messages

    def get_message_info(self, text, bot_url):
        payload = {'query': text}
        payload = json.dumps(payload)

        r = get_request(payload, "http://" + bot_url + "/conversations/default/tracker")
        
        for events in data['events']:
            if 'event' in events:
                if 'action' in events['event']:
                    event_tracker.append(['Utter: ', events['name']])
            if 'parse_data' in events:
                event_tracker.append(['User Message: ', events['text']])
                event_tracker.append(['Intent: ', events['parse_data']['intent']['name']])
                event_tracker.append(['Confidence: ', events['parse_data']['intent']['confidence']])
event_tracker.append('-'*50)
        return message_info