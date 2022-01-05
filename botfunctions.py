import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
import matplotlib.pyplot as plt
from datetime import date
from recipes import *


def get_seven_day(person): 
  with open("{}_seven_day".format(person.name),'r') as fptr:
    seven_day = fptr.readlines()
  return seven_day	

def plot_seven_day(person):
  z = get_seven_day(person)
  weights = [float(element.strip()) for element in z]
  print(weights, len(weights))
  plt.figure(figsize=(12,9))
  plt.title('Seven Day Weight Plot for {}'.format(person.name))
  avg = sum(weights)/len(weights) 

  x1 = [1,2,3,4,5,6,7]
  x2 = [0,1,2,3,4,5,6]
  if person.switch == 0: 
    xs = x2[::-1]
  else: 
    xs = x1[::-1]
  plt.plot(xs[::-1], weights, color='black',linestyle='solid', marker='8', label='Daily Weight')
  plt.rcParams.update({'font.size': 22})
  plt.xlabel('Days ago')
  plt.axhline(y=avg, linestyle='dashed', color='green', label='Average Weight')
  plt.legend()
  plt.ylabel('lbs.', fontsize='22')
  xlabels = [str(element) for element in xs]
  plt.xticks(xs[::-1], labels=xlabels)
  plt.savefig('{}_plot.png'.format(person.name)) 
  plt.clf()
  plt.cla()
  plt.close()
  
def change_macros(message,person):
  today = date.today()
  if is_macro_update(message)[0] == 1:
    content = is_macro_update(message)[1]
    if today != person.daily_macros['day']:
      person.daily_macros = have_not_eaten_yet
    person.daily_macros['calories'] += int(content[0])
    person.daily_macros['protein'] += int(content[1])
    person.daily_macros['fats'] += int(content[2])
    person.daily_macros['carbs'] += int(content[3])
  elif is_macro_update(message)[0] == 2:
    if today != person.daily_macros['day']:
      person.daily_macros = have_not_eaten_yet
    numkey = is_macro_update(message)[1]
    key = numkey[1:]
    recipe = recipe_dict[key]
    num = numkey[0]
    macros = divide_macros(int(num),key)
    person.daily_macros['calories'] += macros[0]
    person.daily_macros['protein'] += macros[1]
    person.daily_macros['fats'] += macros[2]
    person.daily_macros['carbs'] += macros[3]
    print(person.daily_macros)

def divide_macros(number,recipe):
  if recipe in recipe_dict.keys():
    x = [element//number for element in recipe_dict[recipe]]
    return x
  else:
    pass 

def update_weight(person, new_weight): 
  person.weight =  new_weight
  seven_day = get_seven_day(person)
  person.switch = 1
  plot_seven_day(person)
  person.switch = 0
  with open("{}_seven_day".format(person.name),'w') as fptr: 
    fptr.seek(0)
    seven_day.append(str(new_weight)+'\n')
    print(seven_day,'there')
    if len(seven_day) > 7:
      fptr.write(''.join(seven_day[1:]))
    else:
        fptr.write("\n".join(seven_day))
    fptr.truncate()

def reset_macros(person):
  person.daily_macros['calories'] = 0
  person.daily_macros['protein'] = 0
  person.daily_macros['fats'] = 0
  person.daily_macros['carbs'] = 0

def is_weight_update(message):
  msg = message.content.split()
  if len(msg) > 1:
    if msg[1].isnumeric():
      return [1, msg[1]]
    else: 
      return [0, msg[1]]

def is_plot_request(message):
  msg = message.content.split()
  if len(msg) > 1:
    if msg[1] == 'plot':
      return [1, msg[1]]
    else:
      return[0, msg[1]]
    
def is_macro_update(message):
  msg = message.content.split()
  if len(msg) >= 2:
    if msg[1] == 'ate' and '/' in msg[2]:
      return [1, msg[2].split('/')]
    elif msg[1] == 'ate' and msg[2][0].isnumeric():
      return [2, msg[2]]
    else: 
      return [0, msg[1]] 
  else:
    pass 

def is_calorie_reset_request(message):
  msg = message.content.split()
  if len(msg) > 1:
    if msg[1] == 'reset':
      return [1, msg[1]]
    else:
      return[0, msg[1]]
    
def is_help_request(message):
  msg = message.content.split()
  if len(msg) > 1:
    if msg[1] == '?':
      return [1, msg[1]]
    else:
      return[0, msg[1]]
        