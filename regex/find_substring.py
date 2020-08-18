# Day 60 - Problem 66

# Challenge
# Write a Python program to find the occurrence and position of the substrings within a string.

# Example
# Input:
# text = 'Python exercises, PHP exercises, C# exercises'
# pattern = 'exercises'
# Output:
# Found "exercises" at 7:16
# Found "exercises" at 22:31
# Found "exercises" at 36:45


import re


def find_substring(pattern, text):
    for match in re.finditer(pattern, text):
        print('Found "' + pattern + '" at ' + str(match.start()) + ':' + str(match.end()))


text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
find_substring(pattern, text)
