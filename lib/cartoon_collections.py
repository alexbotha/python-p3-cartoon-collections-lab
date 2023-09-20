def roll_call_dwarves(names):
    for i in range(len(names)):
        print(f'{i + 1}. {names[i]}')

def summon_captain_planet(planeteer_calls):
       new = [i.title() + "!" for i in planeteer_calls]
       return new
       

def long_planeteer_calls(words):
    for word in words:
         if len(word) > 4:
              return True 
         
    return False
         
types = ["camembert", "gouda", "cheddar"]

def find_the_cheese(foods):
    
    for food in foods:
        if food in types:
            return food

    return None