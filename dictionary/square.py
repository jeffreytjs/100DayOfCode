# Day 33 - Problem 39

# Challenge
# Write a Python script to print a dictionary where
# 1. the keys are numbers between 1 and 15 (both included)
# 2. the values are square of keys.


square_of_keys = dict(
    [
        (n, n ** 2) for n in range(1, 16)
    ]
)


print(square_of_keys)
