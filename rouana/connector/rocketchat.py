import logging
import threading
import queue
import os


from rasa_core.channels.channel import InputChannel, UserMessage, OutputChannel

logger = logging.getLogger(__name__)

class RocketChatBot(OutputChannel):
    @classmethod
    def name(cls):
        return "rocketchat"

    def __init__(self, user, password, server, ssl):
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
        if not self.logged_in:
            self.connector.login(user=self.user, password=self.password,
                                 callback=self._login_callback)

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
            self.connector.subscribe_to_messages()

    """
    Messages handlers
    """
    def send_text_message(self, recipient_id, message):
        if recipient_id not in self.users:
            self.users[recipient_id] = RocketchatHandleMessages(recipient_id,
                                                                self)
        self.users[recipient_id].add_message(message)

class RocketChatInput(InputChannel):

    """RocketChat input channel implementation."""

    def __init__(self, user=None, password=None,
                 server_url='open.rocket.chat', ssl=True):

        self.user = user
        self.password = password
        self.server_url = server_url
        self.ssl = ssl

        self.rocketchat_bot = RocketChatBot(self.user, self.password,
                                            server=self.server_url,
                                            ssl=self.ssl)

        self.rocketchat_bot.connector.add_prefix_handler('', self.register_message)

        self.message_queue = queue.Queue()

    def start_async_listening(self, message_queue):
        self._record_messages(message_queue.enqueue)

    def start_sync_listening(self, message_handler):
        self._record_messages(message_handler)

    def _record_messages(self, on_message):
        while True:
            if self.rocketchat_bot.logged_in and not self.message_queue.empty():
                msg = self.message_queue.get()

                on_message(
                    UserMessage(msg['msg'], self.rocketchat_bot, msg['rid'])
                )
            else:
                self.rocketchat_bot.login()


    def register_message(self, bot, message):
        self.message_queue.put(message)


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
