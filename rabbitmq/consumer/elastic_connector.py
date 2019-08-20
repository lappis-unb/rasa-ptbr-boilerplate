import logging
import os
import time
import datetime
import hashlib
import json

from elasticsearch import Elasticsearch

try:
    from nltk.corpus import stopwords
except Exception:
    import nltk
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    pass

logger = logging.getLogger(__name__)

ENVIRONMENT_NAME = os.getenv('ENVIRONMENT_NAME', 'locahost')
BOT_VERSION = os.getenv('BOT_VERSION', 'notdefined')
HASH_GEN = hashlib.md5()


def gen_id(timestamp):
    HASH_GEN.update(str(timestamp).encode('utf-8'))
    _id = HASH_GEN.hexdigest()[10:]
    return _id


def get_timestamp():
    ts = time.time()
    timestamp = datetime.datetime.strftime(
        datetime.datetime.fromtimestamp(ts),
        '%Y/%m/%d %H:%M:%S'
    )
    return timestamp


class ElasticConnector():
    def __init__(self, domain,
                 user=None, password=None, scheme='http', scheme_port=80):
        if user is None:
            self.es = Elasticsearch([domain])
        else:
            self.es = Elasticsearch(
                ['{}://{}:{}@{}:{}'.format(scheme, user, password,
                                           domain, scheme_port)],
            )

        self.previous_action = None
        self.previous_user_message = None

    def insert_on_elastic(self, ts, message):
        try:
            self.es.index(index='messages', doc_type='message',
                          id='{}_user_{}'.format(ENVIRONMENT_NAME, gen_id(ts)),
                          body=json.dumps(message))
        except Exception as ex:
            logger.error('Could not send message to Elastic Search')
            logger.error(str(ex))

    def save_user_message(self, user_message):
        if not user_message['text']:
            return

        ts = time.time()
        timestamp = datetime.datetime.strftime(
            datetime.datetime.fromtimestamp(ts),
            '%Y/%m/%d %H:%M:%S'
        )

        # Bag of words
        tags = []
        for word in user_message['text'].replace('. ', ' ') \
                .replace(',', ' ') \
                .replace('"', '') \
                .replace("'", '') \
                .replace('*', '') \
                .replace('(', '') \
                .replace(')', '') \
                .split(' '):
            if word.lower() not in stopwords.words('portuguese') and \
                                                        len(word) > 1:
                tags.append(word)

        message = {
            'environment': ENVIRONMENT_NAME,
            'version': BOT_VERSION,

            'user_id': user_message['sender_id'],
            'is_bot': False,
            'timestamp': timestamp,

            'text': user_message['text'],
            'tags': tags,

            'entities': user_message['parse_data']['entities'],
            'intent_name': user_message['parse_data']['intent']['name'],
            'intent_confidence': (user_message['parse_data']
                                              ['intent']['confidence']),
            'utter_name': '',
            'is_fallback': False,
        }

        self.insert_on_elastic(ts, message)

    def save_bot_message(self, bot_message, action_message, user_message):
        ts = time.time()
        timestamp = datetime.datetime.strftime(
            datetime.datetime.fromtimestamp(ts),
            '%Y/%m/%d %H:%M:%S'
        )

        message = {
            'environment': ENVIRONMENT_NAME,
            'version': BOT_VERSION,
            'user_id': user_message['sender_id'],

            'is_bot': True,

            'text': user_message['text'],
            'tags': [],
            'timestamp': timestamp,

            'entities': [],
            'intent_name': user_message['parse_data']['intent']['name'],
            'intent_confidence': '',

            'utter_name': action_message['name'],
            'is_fallback': action_message['name'] == 'action_default_fallback',
        }

        self.insert_on_elastic(ts, message)
