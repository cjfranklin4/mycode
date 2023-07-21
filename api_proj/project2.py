#!/usr/bin/env python3

import requests
import sys
import os

#Bored API url
bored_url = "http://www.boredapi.com/api/activity/"
activity_type = ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"]
participants = 0

# What should you do today?
def get_user_info():
    while True:
        print("What type of activity would you like to do today? Choose from the list below:")
        for activity in activity_type:
            print(activity, end=" ")
        your_activity = input("\n>").lower().strip()

        if your_activity in activity_type: #validate activity type
            break
        print("Please select an activity from the list below")
    
    while True: #how many people do they want do do it with?
        print("How many people would you like to join you? Choose a number between 1 and 8")
        your_pals = int(input(">"))
        if your_pals in range(1,9):
            break
    while True: #how many activties would you like to be reccomended?
        print("How many reccomendations do you want?")
        recc_num = int(input(">"))
        if type(recc_num) == int:
            break
    return [your_activity, your_pals, recc_num]

user_choice = get_user_info()
print(user_choice)


def call_api(user_choice):
    # set user input information
    activity, pals, num_of_reccs = user_choice
    your_reccs = [];

    ##call the api
    for i in range(num_of_reccs):
        res = requests.get(f"{bored_url}?type={activity}&participants={pals}")
        #print(res.status_code,'status code')
        reccom_activity = res.json()
        if reccom_activity.get('error') != None:
            print(f"Sorry, there is no {activity} activity with {pals} paricipants. Try searching again!")
            sys.exit()
        your_reccs.append(reccom_activity)
        i+= 1

    if pals > 1:
        print(f"Here are some {activity} activity reccomendations for {pals} people:\n")
    else:
        print(f"Here are some {activity} activity reccomendations for one person:\n")
    return your_reccs

get_recss = call_api(user_choice)

# display the user's reccomendations
def display_reccs(reccomends):
    #print(reccomends, 'within display reccs')
    for index, recc in enumerate(reccomends):
        #Print activity name
        acc_name = recc['activity']
        print(f"How about {acc_name}?")

        # Say about how much it should cost
        price = recc['price']
        if price == 0:
            print("Hey, its free!")
        elif price > 0 and price < 0.3:
            print("This is pretty cheap to do!")
        elif price >= 0.3 and price < 0.6:
            print("This seems pretty affordable")
        else:
            print("This might be a bit expensive, but its worth it!")
        # Check for a link to the activity
        if recc['link'] != '':
            print(f"Here is a link to try it: {recc['link']}")
        if index != (len(reccomends) - 1):
            print("\nHere's another one!")

display_reccs(get_recss)

# Save in file for later?
def save_for_later(recc_list):
    while True:#ask if they want to save their reccs in a file for later
        print("\nDo you want to save your reccomendations in a file? Y or N")
        confirm = input("\n>").strip().upper()
        if confirm in ["Y","N"]:
            break
        print("Please choose a valid option.")
    if confirm == "N":#if No, close the program
        print("Hope you enjoyed your reccomendations!")
        sys.exit()
    else:#if yes, write to file in the user's CWD named reccomendations.txt
        print(f"The 'reccomendations.txt' file will be saved to your current directory: {os.getcwd()}")
        with open('reccomendations.txt', 'a') as recc_file:
            print(f"Here is a list of reccomended acitivites for you!\n",file=recc_file)
            for recc in recc_list:
                activity = recc['activity']
                acc_link = recc['link']
                if acc_link != '':
                    print(f"Activity Name: {activity}. Link to learn more: {acc_link}", file=recc_file)
                else:
                    print(f"Activity Name: {activity}", file=recc_file)
        print(f"The 'reccomendations.txt' file has been created in {os.getcwd()}. Enjoy your reccomendations!")

save_for_later(get_recss)
