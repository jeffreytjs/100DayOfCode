# Day 60 - Problem 66

# Challenge
# Write a Python program to check that a string
# contains only a certain set of characters (in this case a-z, A-Z and 0-9).

# Example
# Input: "ABCDEFabcdef123450", "*&%@#!}{"
# Output: True, False


import re


def check_string(my_string):
    if re.findall('[A-Za-z0-9]', my_string) == []:
        return False
    return True


my_string1 = "ABCDEFabcdef123450"
my_string2 = "*&%@#!}{"
print(check_string(my_string1))
print(check_string(my_string2))
