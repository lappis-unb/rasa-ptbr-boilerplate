import logging
import os

from rasa_core.utils import configure_colored_logging, AvailableEndpoints
from rasa_core.run import start_server, load_agent
from rasa_core.interpreter import NaturalLanguageInterpreter
from rasa_core.tracker_store import InMemoryTrackerStore
from rasa_core.broker import PikaProducer

from connector import RocketChatInput

logger = logging.getLogger(__name__)
configure_colored_logging(loglevel='DEBUG')

url = os.getenv('BROKER_URL', '')
username = os.getenv('BROKER_USERNAME', '')
password = os.getenv('BROKER_PASSWORD', '')
queue = os.getenv('QUEUE_NAME', '')

ENABLE_ANALYTICS = os.getenv('ENABLE_ANALYTICS', 'False').lower() == 'true'


def run(core_dir, nlu_dir):
    pika_broker = None

    if ENABLE_ANALYTICS:
        pika_broker = PikaProducer(url,
                                   username,
                                   password,
                                   queue=queue)

    configs = {
        'user': os.getenv('ROCKETCHAT_BOT_USERNAME'),
        'password': os.getenv('ROCKETCHAT_BOT_PASSWORD'),
        'server_url': os.getenv('ROCKETCHAT_URL'),
    }

    input_channel = RocketChatInput(
        user=configs['user'],
        password=configs['password'],
        server_url=configs['server_url']
    )

    _tracker_store = InMemoryTrackerStore(domain=None,
                                          event_broker=pika_broker)

    _endpoints = AvailableEndpoints.read_endpoints(None)
    _interpreter = NaturalLanguageInterpreter.create(nlu_dir)

    _agent = load_agent(core_dir,
                        interpreter=_interpreter,
                        tracker_store=_tracker_store,
                        endpoints=_endpoints)

    http_server = start_server([input_channel], "", "", 5005, _agent)

    try:
        http_server.serve_forever()
    except Exception as exc:
        logger.exception(exc)


if __name__ == '__main__':
    run('/models/dialogue', '/models/nlu/current')
