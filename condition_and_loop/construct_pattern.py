#!/usr/bin/env python
# coding: utf-8
# Day 11 - Problem 14
# In[ ]:


# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
#  Write a Python program to construct the following pattern, using a nested for loop.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

def star_pattern(n):
    """
    Construct a pattern with * such that it increases till n * then decreases.

    :params n: int, maximum number of *
    """
    count = 2
    for i in range(n*2):
        if i <= n:
            print('* '*i)
        else:
            print('* '*(i-count))
            count += 2

star_pattern(5)
