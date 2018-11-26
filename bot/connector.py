import logging
import threading
import os
import time
from typing import Text

from flask import Blueprint, request, jsonify, make_response

from rasa_core.channels.channel import UserMessage, OutputChannel, InputChannel

logger = logging.getLogger(__name__)


class RocketChatBot(OutputChannel):
    @classmethod
    def name(cls):
        return "rocketchat"

    def __init__(self, user, password, server, ssl=False):
        from rocketchat_py_sdk.driver import Driver

        self.username = user
        self.connector = Driver(url=server , ssl=ssl)
        self.users = {}
        self.user = user
        self.password = password

        self.logged_in = False

        self.connector.connect()
        self.login()

    def login(self):
        while not self.logged_in:
            logger.info('Trying to login to rocketchat as {}'.format(self.user))
            self.connector.login(user=self.user, password=self.password,
                                 callback=self._login_callback)
            time.sleep(10)

    """
    Internal callback handlers
    """
    def _login_callback(self, error, data):
        if error:
            logger.error('[-] callback error:')
            logger.error(error)
        else:
            self.logged_in = True
            logger.info("[+] callback success")
            logger.debug(data)

    """
    Messages handlers
    """
    def send_text_message(self, recipient_id, message):
        if recipient_id not in self.users:
            self.users[recipient_id] = RocketchatHandleMessages(recipient_id,
                                                                self)

        for message_part in message.split("\n\n"):
            self.users[recipient_id].add_message(message_part)



class RocketChatInput(InputChannel):
    """RocketChat input channel implementation."""

    @classmethod
    def name(cls):
        return "rocketchat"

    @classmethod
    def from_credentials(cls, credentials):
        if not credentials:
            cls.raise_missing_credentials_exception()

        return cls(credentials.get("user"),
                   credentials.get("password"),
                   credentials.get("server_url"))

    def __init__(self, user, password, server_url):
        # type: (Text, Text, Text) -> None

        self.user = user
        self.password = password
        self.server_url = server_url

        self.output_channel = RocketChatBot(
            self.user, self.password, self.server_url)

    def send_message(self, text, sender_name, recipient_id, on_new_message):
        if sender_name != self.user:
            user_msg = UserMessage(text, self.output_channel, recipient_id,
                                   input_channel=self.name())
            on_new_message(user_msg)

    def blueprint(self, on_new_message):
        rocketchat_webhook = Blueprint('rocketchat_webhook', __name__)

        @rocketchat_webhook.route("/", methods=['GET'])
        def health():
            return jsonify({"status": "ok"})

        @rocketchat_webhook.route("/webhook", methods=['GET', 'POST'])
        def webhook():
            request.get_data()
            if request.json:
                output = request.json

                if "visitor" not in output:
                    sender_name = output.get("user_name", None)
                    text = output.get("text", None)
                    recipient_id = output.get("channel_id", None)
                else:
                    messages_list = output.get("messages", None)
                    text = messages_list[0].get("msg", None)
                    sender_name = messages_list[0].get("username", None)
                    recipient_id = output.get("_id")

                self.send_message(text, sender_name, recipient_id,
                                  on_new_message)

            return make_response()

        return rocketchat_webhook

class RocketchatHandleMessages:
    def __init__(self, rid, bot):
        self.rid = rid
        self.messages = []
        self.message_index = 0
        self.bot = bot
        self.is_typing = False

    def send_message(self):
        msg = self.messages[self.message_index]
        self.message_index += 1

        logger.info('[+] send message {}: {}'.format(self.rid, msg['message']))

        self.bot.connector.send_message(self.rid, msg['message'])

        if self.message_index == len(self.messages):
            if self.is_typing:
                logger.info('deactivate typing for {}'.format(self.rid))

                self.bot.connector.call(
                    'stream-notify-room',
                    [self.rid + '/typing', self.bot.username, False],
                    self.deactivate_typing
                )

            self.messages = []
            self.message_index = 0

    def add_message(self, message):
        if not self.is_typing:
            logger.info('activate typing for {}'.format(self.rid))

            self.bot.connector.call(
                'stream-notify-room',
                [self.rid + '/typing', self.bot.username, True],
                self.activate_typing
            )

        wait_time = int(os.getenv('MIN_TYPING_TIME', 1))
        max_time = int(os.getenv('MAX_TYPING_TIME', 10))

        if len(self.messages) != 0:
            last_msg = self.messages[-1]
            n_words = len(last_msg['message'].split(' '))

            words_per_sec = int(os.getenv('WORDS_PER_SECOND_TYPING', 5))
            wait_time = min(max_time,
                max(1, n_words // words_per_sec)
            ) + last_msg['time']

        threading.Timer(wait_time, self.send_message).start()

        logger.info('[ ] schedule message {}: {}'.format(self.rid, message))
        self.messages.append({'message': message, 'time': wait_time})

    def activate_typing(self, error, data):
        if not error:
            self.is_typing = True

    def deactivate_typing(self, error, data):
        if not error:
            self.is_typing = False

