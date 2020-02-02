#!/usr/bin/env python
# coding: utf-8
# Day 1 - Problem 2
# In[5]:


# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
# Given a collection of intervals which are already sorted by start number, merge all overlapping intervals.
# For example,
# Given [[1,3],[2,6],[5,10],[11,16],[15,18],[19,22]],
# return [[1, 10], [11, 18], [19, 22]]

a = [[1,3],[2,6],[5,10],[11,16],[15,18],[19,22]]

def merge_overlap(input):
    merged = [input[0]]
    for current in input:
        previous = merged[-1]
        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            merged.append(current)
    print(merged)

merge_overlap(a) # Output: [[1, 10], [11, 18], [19, 22]]
