#!/usr/bin/python3
import os

def create_file():
    with ("new_file.txt", "w") as newfile:
        newfile.write("Created a new file!")

def test_create_file():
    assert os.path.exists("new_file.txt") == True