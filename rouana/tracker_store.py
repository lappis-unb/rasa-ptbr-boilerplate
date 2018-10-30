import logging
import os
import time
import datetime
import hashlib
import json

from rasa_core.tracker_store import InMemoryTrackerStore
from rasa_core.events import ActionExecuted, BotUttered, UserUttered

from elasticsearch import Elasticsearch

logger = logging.getLogger(__name__)

es = Elasticsearch([os.getenv('ELASTICSEARCH_URL', 'elasticsearch:9200')])

ENVIRONMENT_NAME = os.getenv('ENVIRONMENT_NAME', 'locahost')
TAIS_VERSION = os.getenv('TAIS_VERSION', 'notdefined')
HASH_GEN = hashlib.md5()

class ElasticTrackerStore(InMemoryTrackerStore):
    def __init__(self, domain):
        super(ElasticTrackerStore, self).__init__(domain)

    def save_user_message(self, tracker, _id):
        if not tracker.latest_message.text:
            return

        message = {
            'environment': ENVIRONMENT_NAME,
            'version': TAIS_VERSION,

            'user_id': tracker.sender_id,
            'is_bot': False,
            'timestamp': time.time(),

            'text': tracker.latest_message.text,

            'entities': tracker.latest_message.entities,
            'intent_name': tracker.latest_message.intent['name'],
            'intent_confidence': tracker.latest_message.intent['confidence'],

            'utter_name': '',
            'is_fallback': False,
        }

        es.index(index='messages', doc_type='message',
                 id='{}_user_{}'.format(ENVIRONMENT_NAME, _id),
                 body=json.dumps(message))

    def save_bot_message(self, tracker, _id):
        if not tracker.latest_message.text:
            return

        utters = []
        index = len(tracker.events) - 1
        while True:
            evt = tracker.events[index]
            if isinstance(evt, UserUttered):
                break
            elif isinstance(evt, BotUttered):
                index -= 1
                utters.append(tracker.events[index].action_name)
            index -= 1


        time_offset = 0
        for utter in utters[::-1]:
            time_offset += 100

            message = {
                'environment': ENVIRONMENT_NAME,
                'version': TAIS_VERSION,
                'user_id': tracker.sender_id,

                'is_bot': True,

                'text': '',
                'timestamp': (datetime.datetime.now() + datetime.timedelta(milliseconds=time_offset)).timestamp(),

                'entities': [],
                'intent_name': '',
                'intent_confidence': '',

                'utter_name': utter,
                'is_fallback': utter == 'action_default_fallback',
            }

            es.index(index='messages', doc_type='message',
                     id='{}_bot_{}'.format(ENVIRONMENT_NAME, _id),
                     body=json.dumps(message))

    def save(self, tracker):
        try:
            HASH_GEN.update(str(time.time()).encode('utf-8'))
            _id = HASH_GEN.hexdigest()[10:]

            self.save_user_message(tracker, _id)
            self.save_bot_message(tracker, _id)
        except Exception as ex:
            logger.error('Could not track messages '
                         'for user {}'.format(tracker.sender_id))
            logger.error(str(ex))

        super(ElasticTrackerStore, self).save(tracker)
