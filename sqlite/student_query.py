

import sqlite3

conn = sqlite3.connect('my_database3.db')

c = conn.cursor()

c.execute('''
    SELECT students.name
    FROM students''')
res = c.fetchall()
student_names = []
for student in res:
    #print(student[0])
    student_names.append(student[0])
#print(res)
print(student_names)
while True:
    print("Students on the Roster:")
    for name in student_names:
        #print(student[0])
        print(name)
    student_name = input("Enter a student name: ").strip()
    if student_name in student_names:
        break
    

c.execute('''
    SELECT courses.name
    FROM courses
    JOIN student_courses ON courses.id = student_courses.course_id
    JOIN students ON students.id = student_courses.student_id
    WHERE students.name = ?''', (student_name,))

courses = c.fetchall()
print(f"{student_name} is taking the following courses:")
for course in courses:
    print(course[0])

conn.close()