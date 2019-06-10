from rasa_core_sdk import Action


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

        dispatcher.utter_message(text)
