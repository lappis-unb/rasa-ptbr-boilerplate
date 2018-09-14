import logging
import os
import yaml

from rasa_core import utils
from rasa_core.interpreter import RasaNLUInterpreter
from connector.rocketchat import RocketChatInput
from rasa_core.agent import Agent

import train

logger = logging.getLogger(__name__)

CREDENTIALS = os.getenv('CREDENTIALS', 'credentials.yml')

def run():
    interpreter = RasaNLUInterpreter('/models/nlu/default/current')
    agent = Agent.load('/models/dialogue', interpreter=interpreter)

    configs = yaml.load(open(CREDENTIALS))

    input_channel = RocketChatInput(
        user=configs['user'],
        password=configs['password'],
        server_url=configs['server_url'],
        ssl=configs['ssl']
    )

    agent.handle_channel(input_channel)


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel='DEBUG')

    logger.info("Train NLU")
    train.train_nlu()
    logger.info("Train Dialogue")
    train.train_dialogue()
    logger.info("Run")
    run()
