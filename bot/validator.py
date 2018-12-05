import logging
import os
from jsonschema import validate
import yaml
from os import listdir
from os.path import isfile, join
from rasa_core import utils
import traceback
import argparse

logger = logging.getLogger(__name__) 

parser = argparse.ArgumentParser()

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

parser.add_argument(
    '--domain', type=str, default='domain.yml',
    help='Path for the domain file'
) 

parser.add_argument(
    '--stories', type=str, default='data/stories.md',
    help='Path for the stories file or directory'
) 

parser.add_argument(
    '--intents', type=str, default='data/intents.md',
    help='Path for the intents file or directory'
)

parser.add_argument(
    '--warnings', '-w', type=str2bool, default=True,
    help='Warings flag'
) 

parser.add_argument(
    '--validate_intents', type=str2bool, default=True,
    help='Run validations to intents'
) 

parser.add_argument(
    '--validate_utters', type=str2bool, default=True,
    help='Run validations to utters'
) 

parser.add_argument(
    '--validate_domain', type=str2bool, default=True,
    help='Run validations to domain'
) 

class Validator:
    domain = ''
    intents = []
    stories = []
    valid_intents = []
    valid_utters = []

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
        file.close()
        try:
            validate(yaml.load(domain_file), yaml.load(schema))
            logger.info('Domain verified')
        except Exception as e:
            logger.error('There is an error in ' + self.domain + ' ' + str(e))


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
            f.close()
    
            for line in intent_lines:
                s_line = line.split(':')
                if len(s_line) == 2 and s_line[0] == '## intent':
                    intents_in_files.append(s_line[1].strip())

        ## Checks if the intents in domain are the same of the ones in the intent files
        for intent in intents_in_domain:
            found = self.search(intents_in_files, intent)
            if not found:
                logger.error('The intent ' + intent + ' is in the domain file but was'+
                          ' not found in the intent files')
            else:
                self.valid_intents.append(intent)
    
        for intent in intents_in_files:
            found = self.search(intents_in_domain, intent)
            if not found:
                logger.error('The intent ' + intent + ' is in the intent files but was'+
                             ' not found in the domain file')

    def verify_intents_in_stories(self):
        if self.valid_intents == []:
            self.verify_intents() 
        

        for file in self.stories:
            f = open(file, 'r')
            stories_lines = f.readlines()
            f.close()

            for line in stories_lines:
                s_line = line.split()
                if len(s_line) == 2 and s_line[0] == '*':  
                    intent = s_line[1]
                    if '{' in intent:
                        intent = intent[:intent.find('{')]
                
                    found = self.search(self.valid_intents, intent)
                    if not found:
                        logger.error('The intent '+ intent +' is used in the stories'+
                                     ' story ile '+ file + ' (line: '+
                                     str(stories_lines.index(line)+1) +
                                     ') but it\'s not a valid intent.')

    def verify_intents_being_used(self):
        if self.valid_intents == []:
            self.verify_intents() 
        
        stories_intents = []
        for file in self.stories:
            f = open(file, 'r')
            stories_lines = f.readlines()
            f.close()

            for line in stories_lines:
                s_line = line.split()
                if len(s_line) == 2 and s_line[0] == '*':
                    intent = s_line[1]
                    if '{' in intent:
                        intent = intent[:intent.find('{')]
                    stories_intents.append(intent)

        for intent in self.valid_intents:
            found = self.search(stories_intents, intent)
            if not found:
                logger.warning('The intent ' + intent + ' is not being used in any story')

    def verify_utters(self): 
        file = open(self.domain, 'r')
        domain_lines = file.readlines()
        file.close()
        utter_actions = []
        utter_templates = []
        
        start = domain_lines.index('templates:\n') + 1
        for i in range(start, len(domain_lines)):
            line = domain_lines[i]
            s_line = line.strip()
            if s_line.split('_')[0] == 'utter':
                utter = s_line
                if utter.endswith(':'):
                    utter = utter[:utter.find(':')]
                utter_templates.append(utter)
            elif (len(s_line.split()) >= 1 and  s_line.split()[0] != '-') and (s_line.endswith(':') and not line.startswith(' ')):
                break

        start = domain_lines.index('actions:\n') + 1
        for i in range(start, len(domain_lines)):
            line = domain_lines[i]
            s_line = line.split()
            if len(s_line) == 2 and s_line[0] == '-':
                ss_line = s_line[1].split('_')
                if ss_line[0] == 'utter':
                    utter_actions.append(s_line[1])
            elif line.strip().endswith(':'):
                break

        for utter in utter_actions:
            found = self.search(utter_templates, utter)
            if not found:
                logger.error('There is no template for utter ' + utter)
            else:
                self.valid_utters.append(utter)
        
        for utter in utter_templates:
            found = self.search(utter_actions, utter)
            if not found:
                logger.error('The utter ' + utter+ ' is not listed in actions')

    def verify_utters_in_stories(self):
        if self.valid_utters == []:
            self.verify_utters() 
        
        for file in self.stories:
            f = open(file, 'r')
            stories_lines = f.readlines()
            f.close()

            for line in stories_lines:
                s_line = line.split()
                if len(s_line) == 2 and s_line[0] == '-':  
                    utter = s_line[1]
                    found = self.search(self.valid_utters, utter)
                    if not found:
                        logger.error('The utter '+ utter +' is used in the stories'+
                                     ' story file '+ file + ' (line: '+
                                     str(stories_lines.index(line)+1) +
                                     ') but it\'s not a valid utter.')

    def verify_utters_being_used(self):
        if self.valid_utters == []:
            self.verify_utters() 
        
        stories_utters = []
        for file in self.stories:
            f = open(file, 'r')
            stories_lines = f.readlines()
            f.close()

            for line in stories_lines:
                s_line = line.split()
                if len(s_line) == 2 and s_line[0] == '-':
                    utter = s_line[1]
                    stories_utters.append(utter)

        for utter in self.valid_utters:
            found = self.search(stories_utters, utter)
            if not found:
                logger.warning('The utter ' + utter + ' is not being used in any story')

    def run_verifications(self):
        self.verify_domain()
        self.verify_intents()
        self.verify_intents_in_stories()
        self.verify_intents_being_used()
        self.verify_utters()
        self.verify_utters_in_stories()
        self.verify_utters_being_used()

if __name__ == '__main__':
    domain = parser.parse_args().domain
    stories = parser.parse_args().stories
    intents = parser.parse_args().intents
    warning = parser.parse_args().warnings
    validate_intents = parser.parse_args().validate_intents
    validate_utters = parser.parse_args().validate_utters
    validate_domain = parser.parse_args().validate_domain

    validator = Validator(domain, intents, stories)
    
    if validate_domain:
        validator.verify_domain()
    
    if validate_intents:
        validator.verify_intents()
        validator.verify_intents_in_stories()
        if warning:
            validator.verify_intents_being_used()

    if validate_utters:
        validator.verify_utters()
        validator.verify_utters_in_stories()
        if warning:
            validator.verify_utters_being_used()
    
