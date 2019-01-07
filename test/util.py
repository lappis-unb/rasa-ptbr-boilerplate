import requests
import logging
import simplejson as json

logger = logging.getLogger(__name__)

"""
The result of the function get_tracker_data() is a list of dictionaries,
where each utter is in a single dict and each user data like user_message,
intent and confidence is in the same dict.
Here is an example of output:

[{'utter': 'action_listen'}, 
{'user_message': 'oi', 'intent': 'cumprimentar', 'confidence': 0.8761389255523682}, 
{'utter': 'utter_cumprimentar'}, 
{'utter': 'utter_menu'}, 
{'utter': 'action_listen'}]
"""

def get_tracker_data():
    URL = 'http://bot:5005/conversations/default/tracker'
    event_tracker = []
    try:
        request = requests.get(url = URL)
        data = request.json()
        for e in data['events']:
            event={}
            if 'event' in e:
                if 'action' in e['event']:
                    event['utter']=e['name']
            if 'parse_data' in e:
                event['user_message']=e['text']
                event['intent']=e['parse_data']['intent']['name']
                event['confidence']=e['parse_data']['intent']['confidence']
            if event != {}:
                event_tracker.append(event)
    except ValueError:
        logger.exception("Error while genting data from RASA API!!")

    return event_tracker

def send_message(message):
    request=""
    try:
        URL = 'http://bot:5005/conversations/default/respond'
        PARAMS = {'query':message}
        request = requests.get(url = URL, params = PARAMS)
    except ConnectionError:
        logger.exception(ConnectionError)
    return request.json()

def send_multiple_messages(messages):
    for userMessage in messages:
        send_message(userMessage)

def start(messages):
    send_multiple_messages(messages)
    logger.exception(get_tracker_data())
    return get_tracker_data()
