# Day 51 - Problem 57

# Challenge
# Write a Python program to generate a series of unique random numbers

import random


def n_random_numbers(n, min_num, max_num):
    result = set()
    while len(result) != n:
        result.add(random.randint(min_num, max_num))
    return result


print(n_random_numbers(5, 10, 10000))
