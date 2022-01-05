from datetime import date
recipe_dict = {
    'ehsf': [2161, 138, 154, 61],
    'csf': [4000, 315, 153, 501],
    'chili': [3567, 265, 146, 311],
    'bs': [3510.280, 145, 271],
    'gccs': [3316, 328, 82, 295],
    'ss': [3869, 282, 134, 380],
    'sj': [5841, 352, 138, 788],
    'gsq': [2951, 298, 99, 314],
    'ccc': [2805, 100, 51, 484],
    'zb': [5177, 70, 244, 688],
    'bb': [3024, 50, 109, 482]
}


today = date.today()

have_not_eaten_yet = {
    'day': today,
    'calories': 0,
    'protein': 0,
    'fats': 0,
    'carbs': 0
}

class person:
    def __init__(self, name, daily_weight, daily_macros, switch):
        self.name = name
        self.weight = daily_weight
        self.daily_macros = daily_macros
        self.switch = switch
        with open("{}_seven_day".format(self.name),'r') as fptr:
          self.seven_day = fptr.readlines()
        #self.seven_day = [str(float(daily_weight)) + '\n'] * 7
        #with open("{}_seven_day".format(self.name), 'w') as fptr:
            #fptr.write(''.join(self.seven_day))
            
Marshall = person("stormcount20", 185, have_not_eaten_yet, 0)
Josie = person("NoniRex", 195, have_not_eaten_yet,0)

person_dict = {'stormcount20': Marshall, 'NoniRex': Josie}
