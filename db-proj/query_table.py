
import sqlite3

conn = sqlite3.connect('my_db.db')
c = conn.cursor()

#Grab days of the week from db
c.execute('''
    SELECT weekdays.weekday
    FROM weekdays''')
res = c.fetchall()
week_list = []
for day in res:
    week_list.append(day[0])

#Prompt for day of the week
while True:
    choice = input("Choose a weekday to see chores list: ").strip().capitalize()
    if choice in week_list:
        break

#Find List of Chores for that Day
c.execute('''
    SELECT chores.type
    FROM chores
    JOIN weekday_chores on chores.id = weekday_chores.chores_id
    JOIN weekdays on weekdays.id = weekday_chores.weekday_id
    WHERE weekdays.weekday = ?
''', (choice,))
chores_day = c.fetchall()

#print(chores_day)
print(f"The list of chores for {choice} is:")
for chore in chores_day:
    print(chore[0])

#Chores list from db
c.execute('''
    SELECT chores.type
    FROM chores''')
res_c = c.fetchall()
chores_list = []
for chore in res_c:
    chores_list.append(chore[0])
#print(chores_list)

#Prompt for chores
while True:
    print("\nChoose a chore to see what day it is planned for: ")
    for chore in chores_list:
        print(chore)
    chore_choice = input(">").strip()
    if chore_choice in chores_list:
        break

#Find all days where that chore is planned for this week
c.execute('''
    SELECT weekdays.weekday
    FROM weekdays
    JOIN weekday_chores on weekdays.id = weekday_chores.weekday_id
    JOIN chores on chores.id = weekday_chores.chores_id
    WHERE chores.type = ?
''', (chore_choice,))
week_days = c.fetchall()

#print(week_days)
print(f"The days of the week for {chore_choice} is:")
for day in week_days:
    print(day[0])

conn.close()
