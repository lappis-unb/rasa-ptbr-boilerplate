from rasa.nlu.components import Component
from rasa.utils.io import json_pickle, json_unpickle
from rasa.nlu.model import Metadata

import nltk
from nltk.classify import NaiveBayesClassifier
from nltk import tokenize, stem
import os

import typing
from typing import Any, Optional, Text, Dict


SENTIMENT_MODEL_FILE_NAME = "sentiment_classifier.pkl"


class SentimentAnalyzer(Component):
    print("Initialised Sentiment Analyzer")

    def __init__(self, component_config=None):
        super(SentimentAnalyzer, self).__init__(component_config)
        self.corpus_words = {}
        self.class_words = {}
        self.stemmer = stem.RSLPStemmer()

    def train(self, training_data, cfg, **kwargs):
        """Load the sentiment polarity labels from the text
        file, retrieve training tokens and after formatting
        data train the classifier."""

        training_data = {}
        import yaml

        with open("/bot/components/labels.yml") as f:
            training_data = yaml.safe_load(f)

        # capture unique stemmed words in the training corpus
        # turn a list into a set (of unique items) and then a list again (this removes duplicates)
        classes = set(list(training_data))
        for c in classes:
            # prepare a list of words within each class
            self.class_words[c] = []

        # loop through each sentence in our training data
        for label, sentences in training_data.items():
            # tokenize each sentence into words
            for sentence in sentences:
                for word in nltk.word_tokenize(sentence, language="portuguese"):
                    # ignore a some things
                    if word not in ["?"]:
                        # stem and lowercase each word
                        stemmed_word = self.stemmer.stem(word.lower())
                        # have we not seen this word already?
                        if stemmed_word not in self.corpus_words:
                            self.corpus_words[stemmed_word] = 1
                        else:
                            self.corpus_words[stemmed_word] += 1

                        # add the word to our words in class list
                        self.class_words[label].append(stemmed_word)

    def convert_to_rasa(self, value, confidence):
        """Convert model output into the Rasa NLU compatible output format."""

        entity = {
            "value": value,
            "confidence": confidence,
            "entity": "sentiment",
            "extractor": "sentiment_extractor",
        }

        return entity

    def calculate_label_score(self, tokens, class_name):
        score = 0
        # tokenize each word in our new sentence
        for word in tokens:
            # check to see if the stem of the word is in any of our classes
            if self.stemmer.stem(word.lower()) in self.class_words[class_name]:
                # treat each word with relative weight
                score += 1 / self.corpus_words[self.stemmer.stem(word.lower())]

        return score

    def process(self, message, **kwargs):
        """Retrieve the tokens of the new message, pass it to the classifier
        and append prediction results to the message class."""

        entity = None

        # calculate a score for a given class taking into account word commonality
        high_class = None
        high_score = 0

        tokens = [t.text for t in message.get("tokens")]

        # loop through our classes
        for class_name in self.class_words.keys():
            # calculate score of sentence for each class
            score = self.calculate_label_score(tokens, class_name)
            # keep track of highest score
            if score > high_score:
                high_class = class_name
                high_score = score

        sentiment = high_class
        confidence = high_score

        entity = self.convert_to_rasa(sentiment, confidence)

        message.set("entities", [entity], add_to_output=True)

    def persist(self, file_name, model_dir):
        """Persist this model into the passed directory."""
        classifier_file = os.path.join(model_dir, SENTIMENT_MODEL_FILE_NAME)
        json_pickle(classifier_file, self)
        return {"classifier_file": SENTIMENT_MODEL_FILE_NAME}

    @classmethod
    def load(
        cls,
        meta: Dict[Text, Any],
        model_dir=None,
        model_metadata=None,
        cached_component=None,
        **kwargs
    ):
        file_name = meta.get("classifier_file")
        classifier_file = os.path.join(model_dir, file_name)
        return json_unpickle(classifier_file)
