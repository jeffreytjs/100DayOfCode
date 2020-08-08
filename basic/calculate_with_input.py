# Day 3 - Problem 6

# Challenge
# Write a Python program that accepts an integer (n)
# and computes the value of n + nn + nnn.

# Example
# Sample value of n is 5
# Expected Result : 615


def calculate_with_input(n):
    print((100 * n) + (2 * 10 * n) + (3 * n))


n = 5
calculate_with_input(n)
