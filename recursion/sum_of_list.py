# Day 58 - Problem 64

# Challenge
# Write a Python program to calculate the sum of a list of numbers. (in recursion fashion)

# Example
# Input: my_list = [1, 3, 5, 6, 10]
# Output: 25


def list_sum(my_list):
    sum = 0
    for i in my_list:
        sum += i
    return sum


my_list = [1, 3, 5, 6, 10]
print(list_sum(my_list))  # 25
