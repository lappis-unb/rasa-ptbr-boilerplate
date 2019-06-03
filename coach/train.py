import logging

from rasa_core import utils, train
from validator import Validator

logger = logging.getLogger(__name__)

utils.configure_colored_logging(loglevel='DEBUG')


def train_dialogue(domain_file,
                   model_path,
                   training_folder,
                   policy_config):
    return train(domain_file=domain_file,
                                      stories_file=training_folder,
                                      output_path=model_path,
                                      policy_config=policy_config,
                                      kwargs={'augmentation_factor': 50,
                                              'validation_split': 0.2,}
                                      )

if __name__ == "__main__":
    validate = Validator('domain.yml','data/intents', 'data/stories/' )
    validate.run_verifications()
    train_dialogue('domain.yml', '/src_models/dialogue', 'data/stories/', 'policy_config.yml')
