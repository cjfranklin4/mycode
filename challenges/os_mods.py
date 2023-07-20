#!/usr/bin/env python3
import os
import shutil

### take input from a user for the files' SOURCE and for the files' DESTINATION
#loops_dir = "/home/student/mycode/copyloops"
#os.chdir(loops_dir)

#loops_dir_content = os.listdir(loops_dir)

user_source = input("What directory would you like to copy files from? \n>")
user_dest = input("What directory would like to copy files to \n>")
confirm_user = input(f"You are moving files from {user_source} to {user_dest}. Is this correct? Y/N: \n>")

## confirm the user's selections
while confirm_user.lower() != "y":
    user_source = input("What directory would you like to copy files from? \n>")
    user_dest = input("What directory would like to copy files to \n>")
    confirm_user = input(f"You are moving files from {user_source} to {user_dest}. Is this correct? Y/N: \n>")

## change to the source directory
####make sure source/dest dir end with /
if user_source.endswith("/") != True:
    user_source = user_source + "/"

if user_dest.endswith("/") != True:
    user_dest = user_dest + "/"

#print(user_source,"source directory")

os.chdir(user_source)
source_content = os.listdir(user_source) #make a list of the contents of the source directory
if os.path.isdir(user_dest) != True:
    os.mkdir(user_dest)

### loop over all the files (file1 file2 file3 file4 file5) in the specified directory (~/mycode/copyloops/), but DON'T move the directory (dontmoveme)
for s_file in source_content:
    if os.path.isdir(user_source + s_file) != True:
       #print(f"Copying{user_source + s_file}")
       shutil.copy(user_source + s_file, user_dest + s_file)
       print(f"Copied {user_source + s_file} to {user_dest + s_file}")

#make a list of user dest contents
dest_content = os.listdir(user_dest)
print("\n")
print("Completed file copying: The updated directories can be found below")
print(f"""
        Source Directory Content:
        {source_content}
        """)
print(f"""
        Destination Directory Content:
        {dest_content}
        """)


### copy the files to another location of your choosing.

