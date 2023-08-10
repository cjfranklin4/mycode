
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

conn.close()