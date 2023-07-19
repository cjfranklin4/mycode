#!/usr/bin/env python3
# Challenge 2
import random

wordbank= ["indentation", "spaces"]
tlgstudents= ['Alex', 'Benji', 'Cayla', 'Demetra', 'Derek', 'Deshawn', 'James', 'Maria', 'Marylyn', 'Nor', 'Sal', 'Sammy']

#part 3
wordbank.append(4)

# part 4 and part 5 (and super bonus)
# check if string is a str only or a number
num = input("Enter an integer from 0 to 11: \n>")
if num.isnumeric() :
    num = int(num)
    if 0 <= num and num < 12:
        student_name = tlgstudents[num]
    else:
        print("The integer you entered is out of range, please choose a integer from 0 to 11.")
        sys.exit()
else:
    student_name = num
# part6
print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")

# Bonus
ran_num = random.randint(0,11)
student_name=tlgstudents[ran_num]
print("Bonus: Random Student")
print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")
