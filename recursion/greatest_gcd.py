# Day 57 - Problem 63

# Challenge
# Write a Python program to find the greatest common divisor (gcd) of two integers.

# Example
# Input: a = 256, b = 56
# Output: 8


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


a = 256
b = 56
print(gcd(a, b))  # 8
