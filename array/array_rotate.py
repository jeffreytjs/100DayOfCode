#!/usr/bin/env python
# coding: utf-8
# Day 4 - Problem 7
# In[3]:


# Rotate an array of n elements to the right by k steps.
# For example, with n = 7 and k = 3,
# the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
# Note:
# Try to come up as many solutions as you can,
# there are at least 3 different ways to solve this problem.

# Method 1: Using two lists
def rotate_arr1(input, steps):
    newList = input[len(input)-(steps%len(input)):]
    newList += input[:len(input)-(steps%len(input))]
    print(newList)
    return newList

# Method 2: Only one list
def rotate_arr2(input, steps):
    while steps>0:
        input.insert(0,input[-1])
        input = input[:-1]
        steps -= 1
    print(input)
    return input

rotate_arr1([1,2,3,4,5,6,7], 20)
rotate_arr1([1,2,3,4,5,6,7,8,9], 20)
