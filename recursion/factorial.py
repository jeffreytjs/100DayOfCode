# Day 56 - Problem 62

# Challenge
# Write a Python program to get the factorial of a non-negative integer.

# Example
# Input: n = 10
# Output: 3628800


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


n = 10
print(factorial(n))
