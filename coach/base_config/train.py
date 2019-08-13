import logging
import os

from rasa_core import utils, train

logger = logging.getLogger(__name__)

utils.configure_colored_logging(loglevel='DEBUG')

AUGMENTATION_FACTOR = int(os.getenv('AUGMENTATION_FACTOR', 50))
VALIDATION_SPLIT = float(os.getenv('VALIDATION_SPLIT', 0.2))


def train_dialogue(domain_file,
                   model_path,
                   training_folder,
                   policy_config):
    return train(domain_file=domain_file,
                                      stories_file=training_folder,
                                      output_path=model_path,
                                      policy_config=policy_config,
                                      kwargs={'augmentation_factor': AUGMENTATION_FACTOR,
                                              'validation_split': VALIDATION_SPLIT,}
                                      )

if __name__ == "__main__":
    train_dialogue('/coach/data/domain.yml', '/src_models/dialogue', '/coach/data/stories/', '/coach/config/policy_config.yml')
