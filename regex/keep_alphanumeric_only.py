# Day 62 - Problem 69

# Challenge
# Write a Python program to remove everything except alphanumeric characters from a string.

# Example
# Input: text = '**//Python Exercises// - 12. '
# Output: PythonExercises12


import re


def check_string(text):
    return ''.join(re.findall('[A-Za-z0-9]', text))


text = '**//Python Exercises// - 12. '
print(check_string(text))
