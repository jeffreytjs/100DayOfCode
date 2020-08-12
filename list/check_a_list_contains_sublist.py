# Day x - Problem x

# Challenge
# Write a Python program to check whether a list contains a sublist.

# Example
"""
Input
a = [2, 4, 3, 5, 7]
b = [4, 3]
c = [3, 7]
Output
print(is_sublist(a, b))
True
print(is_sublist(a, c))
True
"""


def is_sublist(mainlist, sublist):
    is_valid = True
    for i in sublist:
        if i not in mainlist:
            is_valid = False
            return is_valid
    return is_valid


a = [2, 4, 3, 5, 7]
b = [4, 3]
c = [3, 6, 7]
print(is_sublist(a, b))  # True
print(is_sublist(a, c))  # False
