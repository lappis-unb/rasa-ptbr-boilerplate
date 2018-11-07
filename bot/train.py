import logging
import os

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.featurizers import MaxHistoryTrackerFeaturizer, BinarySingleStateFeaturizer, LabelTokenizerSingleStateFeaturizer,FullDialogueTrackerFeaturizer
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy, AugmentedMemoizationPolicy
from rasa_core.policies.fallback import FallbackPolicy
from fallback import CustomFallbackPolicy

logger = logging.getLogger(__name__)
TRAINING_EPOCHS = int(os.getenv('TRAINING_EPOCHS', 20))
NLU_THRESHOLD = float(os.getenv('NLU_THRESHOLD', 0.6))
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
    agent = Agent(domain_file, policies=[
            keras_2,
            MemoizationPolicy(max_history=MAX_HISTORY),
                                                    CustomFallbackPolicy(
                        fallback_action_name=FALLBACK_ACTION_NAME,
                        nlu_threshold=NLU_THRESHOLD,
                        core_threshold=CORE_THRESHOLD)])

    training_data = agent.load_data(training_folder,augmentation_factor=20)

    agent.train(training_data, epochs=TRAINING_EPOCHS)
    agent.persist(model_path)


if __name__ == "__main__":
    train_dialogue('domain.yml', 'models/dialogue', 'data/stories/')
