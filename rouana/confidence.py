import os

from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer, Interpreter
from rasa_nlu import config

intents_directory = './rouana/data/intents/'

training_data = load_data(intents_directory)
trainer = Trainer(config.load('./rouana/config.yml'))
trainer.train(training_data)

model_directory = trainer.persist('./rouana/models/dialogue')
interpreter = Interpreter.load(model_directory)


intents = {}

for intent_file in os.listdir(intents_directory):
    intent_file_path = os.path.join(intents_directory, intent_file)

    intents[intent_file] = {}

    intent_list = []
    intent_name = None

    with open(intent_file_path) as f:
        lines = f.readlines()

        for line in lines:
            line = line.strip()

            if line.startswith('##'):
                if intent_name is not None:
                    intents[intent_file][intent_name] = intent_list
                intent_name = line.replace('## intent:', '')
                intent_list = []

            elif line.startswith('- '):
                intent_list.append(line.replace('- ', ''))

def full_report():
    for intent_file in intents:
        print('File: {}'.format(intent_file))
        print('Number of intents: {}'.format(len(intents[intent_file])))

        for intent in intents[intent_file]:
            intent_list = intents[intent_file][intent]

            print('\n\nIntent: {}'.format(intent))
            print('Number of Examples: {}'.format(len(intent_list)))

            for sample in intent_list:
                print('\nSample: "{}"'.format(sample))
                analisys = interpreter.parse(sample)
                for i in analisys['intent_ranking']:
                    check = ' '
                    if i['name'] == analisys['intent']['name']:
                        check = 'x'
                    print(' {} {:.3f} {}'.format(check, i['confidence'], i['name']))


def interactive():
    while 1:
        inp = input('>>> ')
        inp = inp.strip()

        if inp == 'exit':
            break

        analisys = interpreter.parse(inp)
        for i in analisys['intent_ranking']:
            check = ' '
            if i['name'] == analisys['intent']['name']:
                check = 'x'
            print(' {} {:.3f} {}'.format(check, i['confidence'], i['name']))
        print('\n\n')

if __name__ == '__main__':
    interactive()
