# Day 52 - Problem 58

# Challenge
# Write a Python function to round up a number to specified digits.


def round_up(n, num_digits):
    return round(n, num_digits)


n = 0.123456789
num_digits = 4
print(round_up(n, num_digits))
