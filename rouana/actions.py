from rasa_core.actions.action import Action
from rasa_core.actions.forms import FormAction, EntityFormField, BooleanFormField, FreeTextFormField
from rasa_core.events import SlotSet

# print(tracker.latest_message)
# print(tracker.latest_bot_utterance)
# print(tracker.latest_action_name)
# print(domain.templates)
# print(domain.intents)

class ActionWhatIs(Action):
    def name(self):
        return 'action_what_is'

    def run(self, dispatcher, tracker, domain):
        word_template_map = {
            'proponente': 'Um proponente é bla bla bla bla bla',
            'banana': 'Banana é uma fruta amarela =)',
        }

        user_message = tracker.latest_message.text

        for word in word_template_map:
            if word in user_message:
                dispatcher.utter_message(word_template_map[word])
                return []
        dispatcher.utter_message('Desculpe, não sei conceituar isso ainda =/')
        return []

class ActionSetSlotTrue(Action):
    def name(self):
        return 'action_set_slot_true'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('eh_propenete = True')
        return [SlotSet("eh_propenete", True)]

class ActionSetSlotFalse(Action):
    def name(self):
        return 'action_set_slot_false'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('eh_propenete = False')
        return [SlotSet("eh_propenete", False)]

# print(dir(dispatcher))
# [
#  '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
#  '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
#  '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
#  '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
#  '__str__', '__subclasshook__', '__weakref__', '_fill_template_text',
#  '_template_variables', 'domain', 'latest_bot_messages', 'output_channel',
#  'retrieve_template', 'send_messages', 'sender_id', 'utter_attachment',
#  'utter_button_message', 'utter_button_template', 'utter_custom_message',
#  'utter_message', 'utter_response', 'utter_template'
# ]
# print(dir(tracker))
# [
#  '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
#  '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
#  '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
#  '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
#  '__str__', '__subclasshook__', '__weakref__', '_create_events',
#  '_max_event_history', '_merge_slots', '_paused', '_reset', '_reset_slots',
#  '_set_slot', '_topic_stack', 'applied_events', 'as_dialogue',
#  'clear_follow_up_action', 'copy', 'current_slot_values', 'current_state',
#  'default_topic', 'events', 'events_after_latest_restart', 'export_stories',
#  'export_stories_to_file', 'follow_up_action', 'from_dict',
#  'generate_all_prior_trackers', 'get_latest_entity_values', 'get_slot',
#  'idx_after_latest_restart', 'init_copy', 'is_paused', 'latest_action_name',
#  'latest_bot_utterance', 'latest_message', 'past_states',
#  'previous_topic', 'recreate_from_dialogue', 'replay_events',
#  'sender_id', 'slots', 'topic', 'topics', 'travel_back_in_time',
#  'trigger_follow_up_action', 'update'
# ]
# print(dir(domain))
# [
#  'DEFAULT_ACTIONS', '__abstractmethods__', '__class__', '__delattr__',
#  '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
#  '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
#  '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
#  '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
#  '__subclasshook__', '__weakref__', '_abc_cache', '_abc_negative_cache',
#  '_abc_negative_cache_version', '_abc_registry', '_action_classes',
#  '_action_names', '_actions', '_entities', '_factory_name',
#  '_intents', '_lazy_actions', '_lazy_entities', '_lazy_entity_states',
#  '_lazy_input_state_map', '_lazy_input_states', '_lazy_intent_states',
#  '_lazy_intents', '_lazy_num_actions', '_lazy_prev_action_states',
#  '_lazy_slot_states', '_lazy_slots', '_lazy_templates',
#  '_raise_action_not_found_exception', '_slot_definitions', '_slots',
#  '_templates', 'action_for_index', 'action_for_name', 'action_map',
#  'action_names', 'actions', 'collect_slots', 'collect_templates',
#  'compare_with_specification', 'default_topic', 'entities', 'entity_states',
#  'get_active_states', 'get_parsing_states', 'get_prev_action_states',
#  'index_for_action', 'index_of_state', 'input_state_map', 'input_states',
#  'instantiate_actions', 'intent_states', 'intents', 'load',
#  'load_specification', 'num_actions', 'num_states', 'persist',
#  'persist_specification', 'prev_action_states', 'random_template_for',
#  'restart_intent', 'slot_states', 'slots', 'slots_for_entities',
#  'states_for_tracker_history', 'store_entities_as_slots', 'templates',
#  'topics', 'validate_domain_yaml'
# ]
