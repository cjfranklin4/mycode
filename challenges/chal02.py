#!/usr/bin/env python3
# Challenge 2
import random

wordbank= ["indentation", "spaces"]
tlgstudents= ['Alex', 'Benji', 'Cayla', 'Demetra', 'Derek', 'Deshawn', 'James', 'Maria', 'Marylyn', 'Nor', 'Sal', 'Sammy']

#part 3
wordbank.append(4)

# part 4 and part 5
num = input(" Enter an integer from 0 to 11: \n>")
num = int(num)
student_name = tlgstudents[num]
# part6
print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")

# Bonus
ran_num = random.randint(0,11)
student_name=tlgstudents[ran_num]
print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")
