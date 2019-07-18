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


        # TODO: Inserção das API's sem ser hardcode
        bots = ["localhost:5006", '192.168.100.245:5005']

        # TODO: Paralelizar o envio das mensagens para as APIs cadastradas
        # TODO: Configurar os dados que recebemos do tracker em uma struct separada
        answers = self.ask_bots(text, bots)

        answer = self.get_best_answer(answers)
        # TODO: Continuar com o Fallback padrão quando nenhum bot tem confiança suficiente
        logger.info("Bot: " + answer["bot"])
        logger.info("Confidence: " + str(answer["confidence"]))
        logger.info("Intent Name: " + answer["intent_name"])

        for message in answer["messages"]:
            logger.info("Message: " + message)
            dispatcher.utter_message(message)

        dispatcher.utter_attachment(str(answer))


    def get_best_answer(self, answers):
        # TODO: Fazer a hierarquia das policies, antes da confiança
        max_confidence = max([answer['confidence'] for answer in answers])
        best_answer = {}
        for answer in answers:
            if(answer["confidence"] >= max_confidence):
                best_answer = answer
        return best_answer


    def ask_bots(self, text, bots):
        answers = []
        for bot in bots:
            messages = self.send_message(text, bot)
            info = self.get_answer_info(text, bot)
            bot_answer = {
                "bot": bot,
                "messages": messages,
                "intent_name": info['intent_name'],
                "confidence": info['confidence']
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

    def get_answer_info(self, message, bot_url):
        payload = {'query': message}
        payload = json.dumps(payload)

        r = get_request(payload, "http://" + bot_url + "/conversations/default/tracker")
        answer_info = {}
        for event in r['events']:
            if 'event' in event and 'user' == event['event']:
                if message == event['text']:
                    answer_info['confidence'] = event['parse_data']['intent']['confidence'] 
                    answer_info['intent_name'] = event['parse_data']['intent']['name']
        
        if answer_info == {}:
            answer_info['confidence'] = -1
            answer_info['intent_name'] = "no answer"

        if not answer_info['intent_name']:
            answer_info['intent_name'] = "Fallback"
        
        return answer_info