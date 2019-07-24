from rasa_core_sdk import Action
import json
import environ
import logging
from .api_helper import get_request, post_request
logger = logging.getLogger(__name__)

env = environ.Env()
class ActionTest(Action):
    def name(self):
        return "action_test"

    def run(self, dispatcher, tracker, domain):
        try:
            dispatcher.utter_message("Mensagem enviada por uma custom action.")
        except ValueError:
            dispatcher.utter_message(ValueError)


def get_bots_from_env():
    bot_env_var = env.str("BOTS", "")
    bots = []
    # Remove possible extra ; at the end of the string
    if bot_env_var[-1] == ";":
        bot_env_var = bot_env_var[:-1]

    # Create array of bot name to be used in requests
    for bot in bot_env_var.split(';'):
        bots.append(bot)

    logger.warn("-"*100)
    logger.warn("Signed bots to be requests on fallbacks:\n")
    for bot in bots:
        logger.warn(bot)
    logger.warn("-"*100)

    return bots


class ActionFallback(Action):
    def name(self):
        return "action_fallback"

    def run(self, dispatcher, tracker, domain):
        text = ''
        text = tracker.latest_message.get('text')

        bots = get_bots_from_env()
        # TODO: Inserção das API's sem ser hardcode
        # bots = ["localhost:5006", 'localhost:5007']

        # TODO: Paralelizar o envio das mensagens para as APIs cadastradas
        # TODO: Configurar os dados que recebemos do tracker em uma struct separada
        answers = self.ask_bots(text, bots)

        answer = self.get_best_answer(answers)
        # TODO: Continuar com o Fallback padrão quando nenhum bot tem confiança suficiente
        logger.info("\n\n -- Answer Selected -- ")
        logger.info("Bot: " + answer["bot"])
        logger.info("Confidence: " + str(answer["intent_confidence"]))
        logger.info("Confidence: " + str(answer["utter_confidence"]))
        logger.info("Total Confidence: " + str(answer["total_confidence"]))
        logger.info("Policy: " + str(answer["policy_name"]))
        logger.info("Intent Name: " + answer["intent_name"])

        for message in answer["messages"]:
            logger.info("Message: " + message)
            dispatcher.utter_message(message)

        dispatcher.utter_attachment(str(answer))


    def get_best_answer(self, answers):
        # TODO: Fazer a hierarquia das policies, antes da confiança
        try:
            max_confidence = max([answer['total_confidence'] for answer in answers])
        except ValueError:
            # Empty answers
            max_confidence = 0

        # FIXME: use the value directly from policy_config.yml, smallest of the thresholds
        if(max_confidence >= 0.6):
            best_answer = self.find_answer_by_confidence(answers, max_confidence)
        else:
            best_answer = main_bot_fallback()
        return best_answer

    def find_answer_by_confidence(self, answers, confidence):
        best_answer = {}
        for answer in answers:
            if(answer["total_confidence"] == confidence):
                best_answer = answer

        return best_answer

    def ask_bots(self, text, bots):
        answers = []
        for bot in bots:
            try:
                messages = self.send_message(text, bot)
                info = self.get_answer_info(text, bot)
                if "fallback" in info['policy_name'].lower():    
                    continue
                
                bot_answer = {
                    "bot": bot,
                    "messages": messages,
                    "intent_name": info['intent_name'],
                    "intent_confidence": info['intent_confidence'],
                    "utter_confidence": info['utter_confidence'],
                    "total_confidence": info['intent_confidence']+info['utter_confidence'],
                    "policy_name": info['policy_name'],
                }
                answers.append(bot_answer)
            except:
                logger.warn("Bot didn't answer: " + bot)
                logger.warn("Connection Error")
            
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

        iterator = iter(r['events'])
        for event in iterator:
            if 'event' in event and 'user' == event['event']:
                if message == event['text']:
                    answer_info['intent_confidence'] = event['parse_data']['intent']['confidence'] 
                    answer_info['intent_name'] = event['parse_data']['intent']['name']
                    
                    # always after a user event, there is a action event with policy info.
                    answer_info['utter_confidence'], answer_info['policy_name'] = self.get_policy_info(iterator)

                    break

        if answer_info == {}:
            answer_info['intent_confidence'] = -1
            answer_info['intent_name'] = "no answer"

        if not answer_info['intent_name']:
            answer_info['intent_name'] = "Fallback"
        
        return answer_info
    
    def get_policy_info(self, iterator):
        event = next(iterator)
        if event['event'] != 'action':
            raise ValueError("Event after user event is not a action event")

        return (event['confidence'], event['policy'])