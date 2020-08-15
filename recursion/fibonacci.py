# Day 55 - Problem 61

# Challenge
#  Write a Python program to solve the Fibonacci sequence using recursion.

# Example
# Input: n = 9
# Output: 21


def fibonacci(n):
    try:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    except Exception:
        print(str(n) + "is an invalid value. Input should be >= 1.")


n = 9
print(fibonacci(n))
