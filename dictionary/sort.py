# Day 32 - Problem 38

# Challenge
# Write a Python program to sort (ascending and descending) a dictionary by value.
# Example
"""
Given dictionary:
{0: 0, 1: 2, 2: 1, 3: 4, 4: 3}
Dictionary in ascending order by value:
[(0, 0), (1, 2), (2, 1), (3, 4), (4, 3)]
Dictionary in descending order by value:
[(4, 3), (3, 4), (2, 1), (1, 2), (0, 0)]
"""

d = {0: 0, 1: 2, 2: 1, 3: 4, 4: 3}


def sort_dict_asc(dict):
    list = [(k, v) for k, v in d.items()]
    return sorted(list, key=lambda x: x[1])


def sort_dict_desc(dict):
    list = [(k, v) for k, v in d.items()]
    return sorted(list, key=lambda x: x[1], reverse=True)


print(sort_dict_asc(d))
print(sort_dict_desc(d))
