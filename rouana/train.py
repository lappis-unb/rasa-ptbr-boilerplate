import argparse
import logging
import os

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

logger = logging.getLogger(__name__)
TRAINING_EPOCHS = os.getenv('TRAINING_EPOCHS', 300)

def train_dialogue(domain_file='/rouana/domain.yml',
                   model_path='/models/dialogue',
                   training_data_file='/rouana/data/stories'):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=3), KerasPolicy()])


    training_data = agent.load_data(training_data_file)
    agent.train(
            training_data,
            epochs=int(TRAINING_EPOCHS),
            batch_size=100,
            validation_split=0.2
    )

    agent.persist(model_path)
    return agent


def train_nlu():
    from rasa_nlu.training_data import load_data
    from rasa_nlu import config
    from rasa_nlu.model import Trainer

    training_data = load_data('/rouana/data/intents/')
    trainer = Trainer(config.load('/rouana/config.yml'))
    trainer.train(training_data)
    model_directory = trainer.persist('/models/nlu/',
                                      fixed_model_name='current')

    return model_directory


def run(serve_forever=True):
    interpreter = RasaNLUInterpreter('/models/nlu/default/current')
    agent = Agent.load('/models/dialogue', interpreter=interpreter)

    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())
    return agent


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel='DEBUG')

    parser = argparse.ArgumentParser(
            description='starts the bot')

    parser.add_argument(
            'task',
            choices=['train-nlu', 'train-dialogue', 'run', 'all'],
            help='what the bot should do - e.g. run or train?')
    task = parser.parse_args().task

    # decide what to do based on first parameter of the script
    if task == 'train-nlu':
        train_nlu()
    elif task == 'train-dialogue':
        train_dialogue()
    elif task == 'run':
        run()
    elif task == 'all':
        train_nlu()
        train_dialogue()
        run()

