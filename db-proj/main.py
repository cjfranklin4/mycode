#!/usr/bin/env python3
import sqlite3

conn = sqlite3.connect('my_db.db')
c = conn.cursor()

#Week Table
weekdays = [
    (1, 'Sunday'),
    (2, 'Monday'),
    (3, 'Tuesday'),
    (4, 'Wednesday'),
    (5, 'Thursday'),
    (6, 'Friday'),
    (7, 'Saturday')
]
c.execute('''
    CREATE TABLE IF NOT EXISTS weekdays (
        id INTEGER PRIMARY KEY,
        weekday TEXT NOT NULL
    )
''')
c.executemany('INSERT INTO weekdays VALUES (?, ?)', weekdays)

#Chores Ideas Table
chores = [
    (1, 'Clean Bathroom'),
    (2, 'Wash Dishes'),
    (3, 'Laundry'),
    (4, 'Clean Living Room'),
    (5, 'Take out trash')
]
c.execute('''
    CREATE TABLE IF NOT EXISTS chores (
        id INTEGER PRIMARY KEY,
        chores TEXT NOT NULL
    )
''')
c.executemany('INSERT INTO chores VALUES (?, ?)', chores)

# weekdays_chores Table
weekdays_chores = [
    (1,2,'completed'),
    (1,4,'completed'),
    (2,3,'uncompleted'),
    (2,1,'completed'),
    (3,5,'completed'),
    (3,2,'completed'),
    (4,2,'uncompleted'),
    (4,5,'completed'),
    (5,2,'uncompleted'),
    (5,4,'uncompleted'),
    (6,5,'uncompleted'),
    (6,2,'uncompleted'),
    (7,1,'uncompleted'),
    (7,3,'uncompleted')
]

c.execute('''
    CREATE TABLE IF NOT EXISTS weekday_chores (
        id INTEGER PRIMARY KEY,
        weekday_id INTEGER NOT NULL,
        chores_id INTEGER NOT NULL,
        completed TEXT NOT NULL,
        FOREIGN KEY (weekday_id) REFERENCES weekday (id),
        FOREIGN KEY (chores_id) REFERENCES chores (id)
    )
''')
c.executemany('INSERT INTO weekday_chores (weekday_id, chores_id, completed) VALUES (?, ?, ?)', weekdays)

c.commit()
c.close()