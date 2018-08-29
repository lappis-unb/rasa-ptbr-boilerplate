from rasa_core.actions.action import Action


class ActionOQueEh(Action):
    dont_know_message = 'Desculpe, não sei conceituar isso ainda'

    def name(self):
        return 'action_o_que_eh'

    def run(self, dispatcher, tracker, domain):
        user_message = tracker.latest_message.text.lower()

        for word in self.meaning_map:
            if word in user_message:
                for message in self.meaning_map[word]:
                    dispatcher.utter_message(message)

                return []

        dispatcher.utter_message(self.dont_know_message)
        return []
