# Day 64 - Problem 71

# Challenge
# Remove all whitespaces from a string

# Example
# Input: text= ' Python    Exercises '
# Output: PythonExercises


import re


def remove_spaces(text):
    return re.sub(' ', '', text)


text = ' Python    Exercises '
print(remove_spaces(text))
