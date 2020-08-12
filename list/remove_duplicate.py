# Day 46 - Problem 52

# Challenge
# Write a Python program to remove duplicates from a list.

# Example
# Input: a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
# Output: {40, 10, 80, 50, 20, 60, 30}


def get_unique(my_list):
    return set(my_list)


my_list = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
print(get_unique(my_list))
