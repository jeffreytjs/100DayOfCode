# Day 53 - Problem 59

# Challenge
# Write a Python program to calculate the standard deviation of the following data.

# Example
# Input: my_list = [10, 12, 23, 23, 16, 23, 21, 16]
# Output: 4.8989794855664


def std_dev(my_list):
    n = len(my_list)
    mean = sum(my_list) / n
    variance = sum([((x - mean) ** 2) for x in my_list]) / n
    stddev = variance ** 0.5
    return stddev


my_list = [10, 12, 23, 23, 16, 23, 21, 16]
print(std_dev(my_list))
