#!/usr/bin/env python
# coding: utf-8
# Day 9 - Problem 12
# In[ ]:


# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
# Write a Python program to check a triangle is valid or not

def check_triangle(a, b, c):
    """
    A triangle is valid if the sum of any two sides
    is always greater than the third side.

    :params
    * a : int, side one
    * b : int, side two
    * c : int, side three

    :return boolean True/False
    """
    if (a + b > c) and (a + c > b) and (b + c > a):
        print("1")
        return True
    else:
        print("0")
        return False

check_triangle(1, 10, 12) # Output = False
check_triangle(7, 10, 5)  # Output = True
