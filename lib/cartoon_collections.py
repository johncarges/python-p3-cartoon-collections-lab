def roll_call_dwarves(dwarves):
    for index, name in enumerate(dwarves):
        print(f"{index+1}. {name}")
    pass

def summon_captain_planet(planeteers):
    return [f"{planeteer.capitalize()}!" for planeteer in planeteers]
    pass

def long_planeteer_calls(planeteers):
    return any([len(planeteer)>4 for planeteer in planeteers])
    pass

def find_the_cheese(snacks):
    cheeses = ["cheddar", "gouda", "camembert"]
    for snack in snacks:
        if snack in cheeses:
            return snack
    
    return None

    pass
