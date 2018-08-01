intent_template = '''## intent:{}'''
utter_template = '''class {}(ActionMultiline):
    messages = ['''
answer_template = '''        "{}",'''

def to_camel_case(snake_str):
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)

with open("curiosidades.txt", "r") as source_file:
  lines = source_file.readlines()
  interactions = []
  interaction = ''
  for i in range(0,len(lines)):
    lines[i] = lines[i].strip()
    if lines[i].startswith('Intent:'):
      name = lines[i].split('Intent:')[1].strip()
      interaction = intent_template.format(name)
      interaction += '\n'
    elif lines[i].startswith('Pergunta:'):
      i+=1
      while lines[i].strip().startswith('-'):
        ask = lines[i].strip()
        interaction += ask
        interaction += '\n'
        i+=1
    elif lines[i].startswith('Utter:'):
      if '*****' not in interaction:
        interaction += '*****\n'
      utter = lines[i].split('Utter:')[1].strip()
      utter = to_camel_case(utter)
      interaction += utter_template.format(utter)
      interaction += '\n'
    elif lines[i].startswith('Resposta:'):
      while not lines[i].strip().startswith('\n')and lines[i] != '---\n':
        if(i+1 < len(lines)):
          i+=1
          if lines[i] != '---\n' and lines[i] != '\n':
            answer = lines[i].strip()
            interaction += answer_template.format(answer)
            interaction += '\n'
        else :
          break
    if lines[i] == '---\n':
      interaction += '    ]'
      interactions.append(interaction)

with open("nlu.txt", "w") as nlu_file:
  for inte in interactions:
    nlu_file.write(inte.split('*****')[0])
    nlu_file.write('\n')

with open("actions.txt", "w") as actions_file:
  for inte in interactions:
    actions_file.write(inte.split('*****')[1])
    actions_file.write('\n')
