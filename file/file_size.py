# Day 35 - Problem 41

# Challenge
# Write a Python program to get the file size of a plain file.
# Hint: Use test.txt file within the same folder

import os


def get_filesize(filepath):
    try:
        size = str(os.path.getsize(filepath)) + ' bytes'
        return size

    except Exception:
        print(filepath + ' is not found')


print(get_filesize('test.txt'))
