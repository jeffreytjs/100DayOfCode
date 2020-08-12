# Day 42 - Problem 48

# Challenge
# Write a Python program to get the difference between the two lists

# Example
"""
Input
list1 = [1, 2, 3, 4]
list2 = [1, 2]
Output
[3,4]
"""


def find_difference(list1, list2):
    if len(list1) >= len(list2):
        return [x for x in list1 if x not in list2]
    else:
        return [x for x in list2 if x not in list1]


list1 = [1, 2, 3, 4]
list2 = [1, 2]
print(find_difference(list1, list2))
