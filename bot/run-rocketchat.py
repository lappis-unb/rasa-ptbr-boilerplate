import logging
import os
import yaml

from rasa_core.utils import configure_colored_logging, read_yaml_file, AvailableEndpoints
from rasa_core.run import start_server, load_agent
from rasa_core.interpreter import NaturalLanguageInterpreter
from rasa_core.tracker_store import TrackerStore

from connector import RocketChatInput
from tracker_store import ElasticTrackerStore

logger = logging.getLogger(__name__)
configure_colored_logging(loglevel='DEBUG')

def run(core_dir, nlu_dir):
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

    _endpoints = AvailableEndpoints.read_endpoints(None)
    _interpreter = NaturalLanguageInterpreter.create(nlu_dir)
    _tracker_store = ElasticTrackerStore()

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
    run('models/dialogue', 'models/nlu/current')
