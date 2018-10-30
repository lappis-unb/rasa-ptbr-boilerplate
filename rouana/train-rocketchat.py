import logging
import os
import yaml

from rasa_core import utils
from rasa_core.interpreter import RasaNLUInterpreter
from connector.rocketchat import RocketChatInput
from tracker_store import ElasticTrackerStore
from rasa_core.agent import Agent

from train import *

logger = logging.getLogger(__name__)

CREDENTIALS = path_to_trained_files(os.getenv('CREDENTIALS', 'credentials.yml'))

def run_rocket():
    interpreter = RasaNLUInterpreter(
        path_to_trained_files('models/nlu/default/current')
    )
    tracker = ElasticTrackerStore(path_to_trained_files('models/dialogue'))
    agent = Agent.load(path_to_trained_files('models/dialogue'),
                       interpreter=interpreter, tracker_store=tracker)

    configs = {
        'user': os.getenv('ROCKETCHAT_TAIS_USERNAME'),
        'password': os.getenv('ROCKETCHAT_TAIS_PASSWORD'),
        'server_url': os.getenv('ROCKETCHAT_URL'),
        'ssl': False,
    }

    if not configs['user']:
        if os.path.exists(CREDENTIALS):
            configs = yaml.load(open(CREDENTIALS))
        else:
            logger.error('Could not find credentials file {}'.format(CREDENTIALS))
            return

    input_channel = RocketChatInput(
        user=configs['user'],
        password=configs['password'],
        server_url=configs['server_url'],
        ssl=configs['ssl']
    )

    agent.handle_channel(input_channel)


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel='DEBUG')

    parser = argparse.ArgumentParser(
            description='starts the bot')

    parser.add_argument(
            '--task', '-t', default='all',
            help='what the bot should do - e.g. run or train?')
    task = parser.parse_args().task

    if task == 'train':
        train_nlu()
        train_dialogue()
    elif task == 'run':
        run_rocket()
    elif task == 'all':
        train_nlu()
        train_dialogue()
        run_rocket()
