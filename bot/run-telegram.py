import logging
import os
import train

from rasa_core import utils
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core.channels import InputChannel
from rasa_core.channels.telegram import TelegramInput
from rasa_core.utils import configure_colored_logging, read_yaml_file, AvailableEndpoints
from rasa_core.run import start_server, load_agent
from rasa_core.interpreter import NaturalLanguageInterpreter
from rasa_core.tracker_store import TrackerStore
from tracker_store import ElasticTrackerStore

logger = logging.getLogger(__name__)
configure_colored_logging(loglevel='DEBUG')

def run(core_dir, nlu_dir):

    _endpoints = AvailableEndpoints.read_endpoints('endpoints.yml')
    _interpreter = NaturalLanguageInterpreter.create(nlu_dir)

    input_channel = TelegramInput(
        access_token=os.getenv('TELEGRAM_ACCESS_TOKEN', ''),
        verify=os.getenv('VERIFY', ''),
        webhook_url=os.getenv('WEBHOOK_URL', '')
    )

    elastic_user = os.getenv('ELASTICSEARCH_USER')
    if elastic_user is None:
        _tracker_store = ElasticTrackerStore(
            domain = os.getenv('ELASTICSEARCH_URL', 'elasticsearch:9200')
        )
    else:
        _tracker_store = ElasticTrackerStore(
            domain      = os.getenv('ELASTICSEARCH_URL', 'elasticsearch:9200'),
            user        = os.getenv('ELASTICSEARCH_USER', 'user'),
            password    = os.getenv('ELASTICSEARCH_PASSWORD', 'password'),
            scheme      = os.getenv('ELASTICSEARCH_HTTP_SCHEME', 'http'),
            scheme_port = os.getenv('ELASTICSEARCH_PORT', '80')
        )

    _agent = load_agent(core_dir,
                        interpreter=_interpreter,
                        tracker_store=_tracker_store,
                        endpoints=_endpoints)

    http_server = _agent.handle_channels(
        [input_channel], 5001, ""
    )

    try:
        http_server.serve_forever()
    except Exception as exc:
        logger.exception(exc)

if __name__ == '__main__':
    utils.configure_colored_logging(loglevel='DEBUG')

    logger.info("Train NLU")
    # train.train_nlu()
    logger.info("Train Dialogue")
    train.train_dialogue(
        'domain.yml',
        'models/dialogue',
        'data/stories/',
        'policy_config.yml'
    )
    logger.info("Run")
    run('models/dialogue', 'models/nlu/current')
