# Day 4 - Problem 7

# Challenge
# Rotate an array of n elements to the right by k steps.
# Note:
# Try to come up as many solutions as you can,
# there are at least 3 different ways to solve this problem.

# Examples
# For example, with n = 7 and k = 3,
# the array [1, 2, 3, 4, 5, 6, 7] is rotated to [5, 6, 7, 1, 2, 3, 4].


def rotate_arr1(input, steps):
    """
    Using two lists
    """
    newList = input[len(input) - (steps % len(input)):]
    newList += input[:len(input) - (steps % len(input))]
    return newList


def rotate_arr2(input, steps):
    """
    Using one list
    """
    while steps > 0:
        input.insert(0, input[-1])
        input = input[:-1]
        steps -= 1
    return input


rotate_arr1([1, 2, 3, 4, 5, 6, 7], 20)
rotate_arr2([1, 2, 3, 4, 5, 6, 7, 8, 9], 20)
