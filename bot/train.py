import logging
import os

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.featurizers import MaxHistoryTrackerFeaturizer, BinarySingleStateFeaturizer, LabelTokenizerSingleStateFeaturizer,FullDialogueTrackerFeaturizer
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy, AugmentedMemoizationPolicy
from rasa_core.policies.fallback import FallbackPolicy
from fallback import CustomFallbackPolicy

## imports to verify domain.yml
from jsonschema import validate
import yaml

## imports to verify intents existence
from os import listdir
from os.path import isfile, join

logger = logging.getLogger(__name__)
NLU_THRESHOLD = float(os.getenv('NLU_THRESHOLD', 0.6))

TRAINING_EPOCHS = int(os.getenv('TRAINING_EPOCHS', 20))
BATCH_SIZE = int(os.getenv('BATCH_SIZE', 10))
VALIDATION_SPLIT = float(os.getenv('VALIDATION_SPLIT', 0.2))


CORE_THRESHOLD = float(os.getenv('CORE_THRESHOLD', 0.6))
MAX_HISTORY = int(os.getenv('MAX_HISTORY', 2))
FALLBACK_ACTION_NAME = str(os.getenv('FALLBACK_ACTION_NAME', 'utter_default'))

utils.configure_colored_logging(loglevel='DEBUG')

def train_dialogue(domain_file, model_path, training_folder):
    MemoizationPolicy.USE_NLU_CONFIDENCE_AS_SCORE = True
    #keras_1 = KerasPolicy(
    #             MaxHistoryTrackerFeaturizer(
    #                 BinarySingleStateFeaturizer(),
    #                 max_history=MAX_HISTORY
    #                 )
    #             )
    keras_2 = KerasPolicy(
                FullDialogueTrackerFeaturizer(
                    LabelTokenizerSingleStateFeaturizer()
                )
            )
    #agent = Agent(domain_file, policies=[
    #        keras_2,
    #        MemoizationPolicy(max_history=MAX_HISTORY),
    #                                                CustomFallbackPolicy(
    #                    fallback_action_name=FALLBACK_ACTION_NAME,
    #                    nlu_threshold=NLU_THRESHOLD,
    #                    core_threshold=CORE_THRESHOLD)])

    agent = Agent(domain_file, policies=[
            keras_2,
            MemoizationPolicy(max_history=MAX_HISTORY),
                                                    FallbackPolicy(
                        nlu_threshold=NLU_THRESHOLD,
                        core_threshold=CORE_THRESHOLD)])

    training_data = agent.load_data(training_folder,augmentation_factor=20)

    agent.train(training_data, epochs=TRAINING_EPOCHS, 
                                batch_size=BATCH_SIZE,
                                validation_split=VALIDATION_SPLIT)
    agent.persist(model_path)

def verify_domain():
    schema = """
    type: object
    """
    file = open('domain.yml', 'r')
    domain = file.read()
    validate(yaml.load(domain), yaml.load(schema))
    logger.info('Domain verified')

def search(vector,searched_value):
    vector.append(searched_value)
    count = 0
    while(searched_value != vector[count]):
        count += 1
    if(count == len(vector)-1):
        return('ERROR 404 - ' + searched_value + ' not found')

def verify_intents():
    ## Adds intents in domain to the list
    file = open('domain.yml', 'r')
    domain_lines = file.readlines()
    intents_in_domain = []

    for line in domain_lines:
        if line != 'actions:\n':
            if line[:3] == '  -':
                intents_in_domain.append(line[4:-1])
        else:
            break

    ## Adds intents in intent files to another list
    intents_in_files = []
    intent_files = [f for f in listdir("data/intents") if isfile(join("data/intents", f))]

    for intent in intent_files:
        f = open('data/intents/'+intent, 'r')
        intent_lines = f.readlines()
    
        for line in intent_lines:
            if line[:10] == '## intent:':
                intents_in_files.append(line[10:-1])

    ## Checks if the intents in domain are the same of the ones in the intent files
    for intent in intents_in_domain:
        not_found = search(intents_in_files, intent)
        if not_found:
            logger.error(not_found + ' in intent files')
    
    for intent in intents_in_files:
        not_found = search(intents_in_domain, intent)
        if not_found:
            logger.error(not_found + ' in domain file')
    

if __name__ == "__main__":
    verify_domain()
    verify_intents()
    train_dialogue('domain.yml', 'models/dialogue', 'data/stories/')
