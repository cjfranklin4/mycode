#!/usr/bin/env python3

yuuki= {
    "Yuuki Anzai": {
        "Manga/Anime": "Devil’s Line",
        "Species": ["Devil", "Human"],
        "Birthday": "January 15th 1992",
        "Occupation": {
            "Formerly": "Police Officer for MPD Public Safety Division 5, F Squad",
            "Currently": "Police Officer East Bay Public Security Section 1, Squad 3"
        }
    }
}

# add new key-value pair
yuuki["Yuuki Anzai"].update({"Age":21})

# print all keys
yuu_keys = list(yuuki["Yuuki Anzai"].keys())
print(yuu_keys)

#choose a key
choice = input("Choose a key from the list above: \n>")
yuu_obj = yuuki["Yuuki Anzai"]
if yuu_obj.get(choice) == None:
    #valid_key = input("Please input a valid key: \n")
    print("Please input a valid key")
    while choice == None:
        choice
else:
    # return key and value
    choice_val = yuuki["Yuuki Anzai"].get(choice)
    name = list(yuuki.keys())
    print(f"{name[0]}'s {choice} is: {choice_val}")
