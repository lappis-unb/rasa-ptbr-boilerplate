#!/usr/bin/env python3

import argparse
import logging
import time

from rocketchat_py_sdk.driver import Driver

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
    '--user-name', '-un', type=str, default='tais',
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

args = parser.parse_args()

host = args.rocketchat_url
if host[-1] == '/':
    host = host[:-1]

bot = {
    'username': args.user_name,
    'password': args.user_password,
    'driver': None,
}

ssl_config = args.ssl

channels_ids = []


def connect_bot():

    def login_callback(error, data):
        if error:
            logger.error('Could not login as {}'.format(bot))
            logger.error(error)
            return

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

    messages = map(lambda message: {
            'username': message['u']['username'],
            'text': message['msg'],
            'timestamp': message['ts'], 
        },
        data['messages']
    )

    room = {'id': room_id, 'messages': list(messages)}
    logger.info('Got {} messages for room {}'.format(
        len(room['messages']), room_id)
    )


if __name__ == '__main__':
    connect_bot()

    while True:
        time.sleep(10)