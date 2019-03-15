#!/usr/bin/env python3

import logging
import time
import os
import json
import queue
import requests

from rocketchat_py_sdk.driver import Driver

logger = logging.getLogger('Parse Chats History')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s'
)

ch.setFormatter(formatter)

logger.addHandler(ch)


bot = {
    'bot_url': os.getenv('BOT_URL', 'http://bot:5005/webhooks/rest/webhook'),
    'rocketchat_url': os.getenv('ROCKETCHAT_URL', 'rocketchat:3000'),
    'username': os.getenv('ROCKETCHAT_BOT_USERNAME', 'bot'),
    'password': os.getenv('ROCKETCHAT_BOT_PASSWORD', 'bot'),
    'driver': None,
}

logged_in = False

def connect_bot():
    def login_callback(error, data):
        global logged_in

        if error:
            logger.error('Could not login as {}'.format(bot['username']))
            logger.error(error)
            return

        if not logged_in:
            logger.info('Login succesful')
            logged_in = True
            get_user_rooms()

    logger.info('Trying to login as {}'.format(bot['username']))
    bot['driver'] = Driver(url=bot['rocketchat_url'], ssl=False)
    bot['driver'].connect()
    bot['driver'].login(user=bot['username'], password=bot['password'], callback=login_callback)


def get_user_rooms():
    def rooms_callback(error, data):
        if error:
            logger.error('Could not get rooms as {}'.format(bot['username']))
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
            replay_room
        )

def replay_room(error, data):
    if error:
        logger.error(error)
        return

    room_id = data['messages'][0]['rid']

    print("---- Replay room {} ----".format(room_id))

    bot_queue = queue.Queue()

    for message in data['messages'][::-1]:
        expected_answer = None
        user_msg = ""

        if message['u']['username'] != bot['username']:
            print('User said: {}'.format(message['msg']))

            res = requests.post(bot['bot_url'], json={
                'sender': message['u']['_id'],
                'message': message['msg'],
            })

            if res.status_code == 200:
                for answer in res.json():
                    bot_queue.put(answer['text'])

        else:
            print("Bot answered on chat: {}".format(message['msg']))

            expected_answer = 'xxxx No more answers xxxx'
            if bot_queue.qsize() != 0:
                expected_answer = bot_queue.get()

            print("Expected answer now: {}".format(expected_answer))

            if expected_answer != message['msg']:
                print('!!! The current answer differ from the given on the chat')
                print('Should I proceed?')


if __name__ == '__main__':

    while not logged_in:
        connect_bot()
        time.sleep(10)

    while True:
        time.sleep(10)

