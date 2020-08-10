# Day 34 - Problem 40

# Challenge
# Sum all the items in a dictionary

# Example
# Input: {'data1': 100, 'data2': -54, 'data3': 247}
# Output: 293


def sum_all_items(dict):
    sum = 0
    for key in dict:
        sum += dict[key]
    return sum


dict = {'data1': 100, 'data2': -54, 'data3': 247}
print(sum_all_items(dict))
