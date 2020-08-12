# Day 41 - Problem 47

# Challenge
# Write a Python program to find common items from two lists.

# Example
"""
Input
color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]
Output
['Green', 'White']
"""


def find_common(list1, list2):
    if len(list1) >= len(list2):
        return [x for x in list1 if x not in list2]
    else:
        return [x for x in list2 if x not in list1]


color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]
print(find_common(color1, color2))
