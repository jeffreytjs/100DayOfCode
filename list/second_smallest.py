# Day 47 - Problem 53

# Challenge
# Write a Python program to find the second smallest number in a list.

# Example
# Input: my_list = [1, 2, -8, -2, 0]
# output: -2


def second_smallest(my_list, n):
    """
    Introduced n such that any n-th smallest element can be retrieved
    """
    try:
        my_list.sort()
        return my_list[n - 1]
    except Exception:
        print(str(n) + ' is not a valid index. Use an index of <=' + str(len(my_list)))


my_list = [1, 2, -8, -2, 0]
print(second_smallest(my_list, 8))
