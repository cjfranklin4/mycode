#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

# Part 1
print("PART 1")
def ne_farm():
    NE_animals = farms[0]["agriculture"]
    for animal in NE_animals:
        print(animal)

ne_farm()

# Part 2
print("\nPART 2")
farm_names = []
def get_farm_names():
    for farm in farms:
        farm_names.append(farm["name"].lower())
get_farm_names()
#print(farm_names)

def print_farm_names():
    for farm in farms:
        print(f'{farm["name"]}')

def choose_farm():
    print_farm_names()
    user_farm = input(f"Choose a farm: ")
    while user_farm.lower().strip() not in farm_names:
        print_farm_names()
        user_farm = input("Please choose a valid farm: ")
    #Update the farm name value and grab its index within the list
    farm_index = 0
    for index, farm in enumerate(farms):
        if user_farm.lower().strip() == farm["name"].lower():
            user_farm = farm["name"]
            farm_index = index
    
    #Print the farm plant/animal list
    print(f"\n{user_farm}'s agricultural items are:")
    user_farm_ag = farms[index]["agriculture"]
    for ag in user_farm_ag:
        print(ag)

choose_farm()
# Part 3
