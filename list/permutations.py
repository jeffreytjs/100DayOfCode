# Day 45 - Problem 51

# Challenge
# Write a Python program to generate all permutations of a list in Python

# Example
# Input: my_list = [1, 2, 3]
# Output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

import itertools


# Using library
def permutate_lib(my_list):
    return list(itertools.permutations(my_list))


my_list = [1, 2, 3]
print(permutate_lib(my_list))
