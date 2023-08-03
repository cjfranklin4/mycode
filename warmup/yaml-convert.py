#!/usr/bin/env python3
import yaml
import json

def main():
    with open("favs.json", "r") as favs:
        fav_list = json.load(favs)
    #print(fav_list)
    me= {'name': 'Cayla', 'movie': 'Napoleon Dynamite', 'ice cream': 'none', 'color': 'Blue'}
    fav_list.append(me)
    print(fav_list)

    #convert to YAML
    with open("favs.yaml", "w") as fav_yaml:
        yaml.dump(fav_list, fav_yaml)
if __name__ == "__main__":
    main()