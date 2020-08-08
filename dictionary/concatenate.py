# Day 30 - Problem 36

# Challenge
# Write a Python script to concatenate following dictionaries to create a new one
# Example
"""
Sample input:
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
Sample output:
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""

# Reference from https://stackoverflow.com/questions/38987/how-do-i-merge-two-dictionaries-in-a-single-expression-in-python/26853961#26853961 # noqa
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
z = {**dic1, **dic2, **dic3}
print(z)
