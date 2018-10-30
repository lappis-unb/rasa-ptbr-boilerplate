#!/usr/bin/env python3

import argparse
import logging
import time
import datetime
import os
import json
import pprint

from rocketchat_py_sdk.driver import Driver

from elasticsearch import Elasticsearch

from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer, Interpreter
from rasa_nlu import config

# == Log Config ==

logger = logging.getLogger('Parse Chats History')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s'
)

ch.setFormatter(formatter)

logger.addHandler(ch)

# == CLI ==

parser = argparse.ArgumentParser()

parser.add_argument(
    '--username', '-un', type=str, default='tais',
    help='Bot username (default: tais)'
)
parser.add_argument(
    '--user-password', '-up', type=str, default='tais',
    help='Bot password (default: tais)'
)
parser.add_argument(
    '--rocketchat-url', '-r', type=str, default='localhost:3000',
    help='Rocket chat URL (default: http://localhost:3000)'
)
parser.add_argument(
    '--ssl', '-s', type=bool, default=False,
    help='Web Socker SSL config (default: False)'
)
parser.add_argument(
    '--intents-directory', '-id', type=str, default='/rouana/data/intents/',
    help='Directory where the intents are (default: /rouana/data/intents/)'
)
parser.add_argument(
    '--rasa-config', '-rc', type=str, default='/rouana/config.yml',
    help='Rasa configuration file (default: /rouana/config.yml)'
)
parser.add_argument(
    '--model-directory', '-md', type=str, default='/models/dialogue',
    help='Directory where the training data will persist (default: /models/dialogue)'
)
parser.add_argument(
    '--environment-name', '-e', type=str, default='localhost',
    help='Environment\'s name where the data will be extracted (default: localhost)'
)

args = parser.parse_args()

host = args.rocketchat_url
if host[-1] == '/':
    host = host[:-1]

bot = {
    'username': args.username,
    'password': args.user_password,
    'driver': None,
}

ssl_config = args.ssl

environment_name = args.environment_name.replace(' ', '_')
interpreter = None
logged_in = False

es = Elasticsearch([os.getenv('ELASTICSEARCH_URL', 'elasticsearch:9200')])

def connect_bot():
    def login_callback(error, data):
        global logged_in

        if error:
            logger.error('Could not login as {}'.format(bot))
            logger.error(error)
            return

        if not logged_in:
            logger.info('Login succesful')
            logged_in = True
            get_user_rooms()

    logger.info('Trying to login as {}'.format(bot))
    bot['driver'] = Driver(url=host, ssl=ssl_config)
    bot['driver'].connect()
    bot['driver'].login(user=bot['username'], password=bot['password'], callback=login_callback)


def get_user_rooms():
    def rooms_callback(error, data):
        if error:
            logger.error('Could not get rooms as {}'.format(bot))
            logger.error(error)
            return

        rooms = list(filter(lambda room: room['t'] == 'l', data))

        logger.info('Found {} rooms, and {} of '
                    'them are from the livechat'.format(len(data), len(rooms)))
        get_rooms_history(rooms)

    logger.info('Getting rooms from ' + bot['username'])
    bot['driver'].call('rooms/get', [], rooms_callback)


def get_rooms_history(rooms):
    for room in rooms:
        room_id = room['_id']
        logger.info('Get messages for room {}'.format(room_id))

        bot['driver'].call(
            'loadHistory',
            [ room_id, None, 1000, None ],
            enrich_data
        )

def enrich_data(error, data):
    if error:
        logger.error(error)
        return

    room_id = data['messages'][0]['rid']

    for message in data['messages']:
        message_id = environment_name + '::' + message['_id']

        message = {
            'environment': environment_name,
            'room_id': room_id,

            'username': message['u']['username'],
            'is_bot': message['u']['username'] == args.username,

            'text': message['msg'],
            'timestamp': str(message['ts'].strftime('%Y-%m-%d %H:%M:%S')),

            'entities': [],
            'intents': [],
        }

        if not message['is_bot']:
            nlu_data = interpreter.parse(message['text'])
            message['entities'] = nlu_data['entities']
            message['intents']  = nlu_data['intent_ranking']

        logger.info('Indexing message {} {}'.format(message_id,
                                                    message['text']))

        es.index(index='messages', doc_type='message',
                 id=message_id, body=json.dumps(message))


if __name__ == '__main__':
    training_data = load_data(args.intents_directory)
    trainer = Trainer(config.load(args.rasa_config))
    trainer.train(training_data)

    logger.info('Model training ended')

    model_directory = trainer.persist(args.model_directory)
    interpreter = Interpreter.load(model_directory)

    while not logged_in:
        connect_bot()
        time.sleep(10)

    while True:
        time.sleep(10)
