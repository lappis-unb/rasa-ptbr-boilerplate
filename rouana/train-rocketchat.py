import logging
import os
import yaml

from rasa_core import utils
from rasa_core.interpreter import RasaNLUInterpreter
from connector.rocketchat import RocketChatInput
from rasa_core.agent import Agent

from train import *

logger = logging.getLogger(__name__)

CREDENTIALS = path_to_trained_files(os.getenv('CREDENTIALS', 'credentials.yml'))

def run_rocket():
    interpreter = RasaNLUInterpreter(
        path_to_trained_files('models/nlu/default/current')
    )
    agent = Agent.load(path_to_trained_files('models/dialogue'),
                                             interpreter=interpreter)

    configs = yaml.load(open(CREDENTIALS))

    username = os.getenv('TAIS_USERNAME', configs['user'])
    password = os.getenv('TAIS_PASSWORD', configs['password'])
    url = os.getenv('ROCKETCHAT_URL', configs['server_url'])

    input_channel = RocketChatInput(
        user=username,
        password=password,
        server_url=url,
        ssl=configs['ssl']
    )

    agent.handle_channel(input_channel)


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel='DEBUG')

    logger.info("Train NLU")
    train_nlu()
    logger.info("Train Dialogue")
    train_dialogue()
    logger.info("Run")
    run_rocket()
