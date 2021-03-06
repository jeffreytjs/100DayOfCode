# Day 6 - Problem 9

# Challenge
# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
# You may assume that each input would have exactly one solution

# Examples
# Given nums = [2, 7, 11, 15], target = 26,
# Because nums[2] + nums[3] = 11 + 15 = 26,
# return [2, 3].


def sum_of_two(arr, t):
    '''
    Assuming exactly one solution, takes in an array of integers and a target
    which is a sum of two integers within the array.

    Returns a list containing the index of the two integers.
    '''
    newList = []
    for i in range(len(arr)):
        difference = t - arr[i]
        if difference in arr:
            newList.append(i)
            newList.append(arr.index(difference))
            break
    return newList


arr = [2, 7, 11, 15]
t = 26
sum_of_two(arr, t)
