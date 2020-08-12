# Day 44 - Problem 50

# Challenge
# Write a Python program to get the frequency of the elements in a list.

# Example
# Input: my_list = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]
# Outout: {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}


def list2dict(my_list):
    my_dict = {}
    for i in my_list:
        if i not in my_dict.keys():
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    return my_dict


my_list = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]
print(list2dict(my_list))
