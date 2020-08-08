# Day 29 - Problem 35

# Challenge
# Check if a given key already exists in a dictionary
# Example
"""
Given: d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

Sample input: is_key_present(5)
Sample output: Key is present in the dictionary

Sample input: is_key_present(9)
Sample output: Key is not present in the dictionary
"""

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def is_key_present(key):
    if key in d.keys():
        return str(key) + " is present in the dictionary"
    else:
        return str(key) + " is not present in the dictionary"


is_key_present(5)
is_key_present(9)
