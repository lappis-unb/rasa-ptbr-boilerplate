import logging
import os
from jsonschema import validate
import yaml
from os import listdir
from os.path import isfile, join
from rasa_core import utils

class Validator:
    domain = ''
    intents = []
    stories = []
    valid_intents = []

    def __init__(self, domain_path, intents_path, stories_path):
        self.domain = domain_path

        if os.path.isfile(intents_path):
            self.intents.append(intents_path)

        elif os.path.isdir(intents_path):
            if not intents_path.endswith('/'):
                intents_path += '/'

            intent_files = [f for f in listdir(intents_path) if isfile(join(intents_path, f))]
            for file in intent_files:
                self.intents.append(intents_path + file)
                     
        if os.path.isfile(stories_path):
            self.stories.append(stories_path)

        elif os.path.isdir(stories_path):
            if not stories_path.endswith('/'):
                stories_path += '/'

            stories_files = [f for f in listdir(stories_path) if isfile(join(stories_path, f))]
            for file in stories_files:
                self.stories.append(stories_path + file)

    def verify_domain(self):
        schema = """
        type: object
        """
        file = open(self.domain, 'r')
        domain_file = file.read()
        validate(yaml.load(domain_file), yaml.load(schema))
        logging.info('Domain verified')
        file.close()

    def search(self, vector,searched_value):
        vector.append(searched_value)
        count = 0
        while(searched_value != vector[count]):
            count += 1
        if(count == len(vector)-1):
            return False
        else:
            return True

    def verify_intents(self):
        ## Adds intents in domain to the list
        file = open(self.domain, 'r')
        domain_lines = file.readlines()
        file.close()
        intents_in_domain = []
        intents_in_files = []
    
        start = domain_lines.index('intents:\n') + 1

        for i in range(start, len(domain_lines)):
            line = domain_lines[i]
            s_line = line.split()
            if len(s_line) == 2 and s_line[0] == '-':
                intents_in_domain.append(s_line[1])
            elif line.strip().endswith(':'):
                break

        ## Adds intents in intent files to another list
        for intent in self.intents:
            f = open(intent, 'r')
            intent_lines = f.readlines()
    
            for line in intent_lines:
                s_line = line.split(':')
                if len(s_line) == 2 and s_line[0] == '## intent':
                    intents_in_files.append(s_line[1].strip())

        ## Checks if the intents in domain are the same of the ones in the intent files
        for intent in intents_in_domain:
            found = self.search(intents_in_files, intent)
            if not found:
                logging.error('Intent ' + intent + ' is in the domain file but was'+
                          ' not found in the intent files')
            else:
                self.valid_intents.append(intent)
    
        for intent in intents_in_files:
            found = self.search(intents_in_domain, intent)
            if not found:
                logging.error('Intent ' + intent + ' is in the intent files but was'+
                             ' not found in the domain file')
            else:
                self.valid_intents.append(intent)

    def verify_intents_in_stories(self):
        for file in self.stories:
            f = open(file, 'r')
            stories_lines = f.readlines()
    
            for line in stories_lines:
                s_line = line.split()
                if len(s_line) == 2 and s_line[0] == '*':  
                    intent = s_line[1]
                    if '{' in intent:
                        intent = intent[:intent.find('{')]
                
                    found = self.search(self.valid_intents, intent)
                    if not found:
                        logging.error('The intent'+ intent +' is used in the stories'+
                                     ' file '+ file + ' (line:'+
                                     str(stories_lines.index(line)+1) +
                                     ' ) but it\'s not a valid intent.')

    def run_verifications(self):
        self.verify_domain()
        self.verify_intents()
        self.verify_intents_in_stories()

