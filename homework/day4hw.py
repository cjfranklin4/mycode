#!/usr/bin/env python3
import random

# Importing Modules
print("Importing Modules")
ran_a = random.randint(1,6)
ran_b = random.randint(1,6)

if ran_a > ran_b:
    print("Random A won!")
elif ran_a < ran_b:
    print("Random B won!")
else:
    print("Its a tie!")

# For Loops
print("For Loops")
## can you loop over this list and print "<hero name> is great!"
heroes= ["Batman","Spiderman","Catwoman","Alfred Pennyworth"]
def loop_heroes():
    for hero in heroes:
        print(f"{hero} is great!")
loop_heroes()
print("\n")
## can you loop over this list of dictionaries are print: "<hero name>'s power is <power>"
hero_dict= [{"name": "Batman", "powers": "being the world's greatest detective"},
            {"name": "Spiderman", "powers": "web shooting"},
            {"name": "Catwoman", "powers": "burglary"},
            {"name": "Alfred Pennyworth", "powers": "being super butler"}
           ]
print("\n")
def loop_dict():
    for hero in hero_dict:
        print(f'{hero["name"]}\'s power is {hero["powers"]}')
loop_dict()

# Reading/Writing to files
print("Reading/Writing to Files")

def file_prac():
    with open("simpledoc.txt", "r") as simplefile:
        simplelist = simplefile.readlines()
        for line in simplelist:
            print(line, end="")
        print(simplelist)
    with open("simpledoc.txt","a") as simplefile:
        simplefile.write("This is a new line")

file_prac()
