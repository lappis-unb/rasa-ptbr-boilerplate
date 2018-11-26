import pytest
import requests
import simplejson as json

def send_message(message):
    request=""
    try:
        URL = 'http://localhost:5005/conversations/default/respond'
        PARAMS = {'query':message}
        request = requests.get(url = URL, params = PARAMS)
    except ConnectionError:
        print(ConnectionError)
    return request.json()

def get_data():
    URL = 'http://localhost:5005/conversations/default/tracker'
    event_tracker = []
    try:
        request = requests.get(url = URL)
        data = request.json()
        for e in data['events']:
            if 'event' in e:
                if 'action' in e['event']:
                    event_tracker.append(['utter', e['name']])
            if 'parse_data' in e:
                event_tracker.append(['user_message', e['text']])
                event_tracker.append(['intent', e['parse_data']['intent']['name']])
                event_tracker.append(['confidence', e['parse_data']['intent']['confidence']])
    except ValueError:
        print("Error while genting data from RASA API!!")

    return event_tracker

def send_multiple_messages(messages):
    for userMessage in messages:
        send_message(userMessage)

def test_cumprimentar():
    multiplePaths = ['oi', 'o que é salic?']
    send_multiple_messages(multiplePaths)
    print(get_data())
    assert get_data()[2][1] == 'cumprimentar'

def test_salic():
    assert get_data()[8][1] == 'definicao_salic'

