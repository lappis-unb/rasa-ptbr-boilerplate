with open("curiosidades.txt", "r") as source_file:
  lines = source_file.readlines()
  interactions = []
  interaction = ''
  names = []
  actions = []

  interaction = {
    'intent': '',
    'questions': [],
    'answers': [],
  }

  on_questions = False
  on_answers = False
  for i in range(0,len(lines)):
    line = lines[i].strip()

    if '---' in line:
      interactions.append(interaction)
      interaction = {
        'intent': '',
        'questions': [],
        'answers': [],
      }
      on_questions = False
      on_answers = False

    elif line == '':
      continue

    elif line.startswith('Intent:'):
      interaction['intent'] = line.replace('Intent:', '').strip()
      on_questions = True

    elif on_questions and line.startswith('- '):
      interaction['questions'].append(line[2:])

    elif line.startswith('Resposta:'):
      on_questions = False
      on_answers = True

    elif on_answers:
      interaction['answers'].append(line)

print(interactions)

def to_camel_case(snake_str):
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)

with open("nlu.txt", "w") as f:
  for i in interactions:
    f.write('## intent:{}\n'.format(i['intent']))
    for q in i['questions']:
      f.write('- {}\n'.format(q))
    f.write('\n')

with open("actions.txt", "w") as f:
  for i in interactions:
    f.write('class Action{}(ActionMultiline):\n'.format(to_camel_case(i['intent'])))
    f.write('    messages = [\n')

    for a in i['answers']:
      f.write("        '{}',\n".format(a))
    f.write('    ]\n\n')

with open("domain.txt", "w") as f:
  f.write('intents:\n')
  for i in interactions:
    f.write('  - {}\n'.format(i['intent']))

  f.write('\nactions:\n')
  for i in interactions:
    f.write('  - rouana.actions_curiosidades.Action{}\n'.format(to_camel_case(i['intent'])))

with open("stories.txt", "w") as f:
  story_temaplate = '''## path1.{}
> identifica_perfil
* {}
  - Action{}
  - ActionCuriosidadesMais
> curiosidade_final\n\n
'''
  count = 0
  for i in interactions:
    f.write(story_temaplate.format(count, i['intent'], to_camel_case(i['intent'])))
    count += 1
