def roll_call_dwarves(list):
    for name in list:
        print(f"{list.index(name) + 1}. {name}")

def summon_captain_planet(list):
    return [element.capitalize() + "!" for element in list]

def long_planeteer_calls(list):
    for word in list:
        if len(word) > 4:
            return True
    return False

def find_the_cheese(list):
    for element in list:
        if element == 'cheddar' or element == 'gouda' or element == 'camebert':
            return element
    
    return None
