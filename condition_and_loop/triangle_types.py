#!/usr/bin/env python
# coding: utf-8
# Day 16 - Problem 19
# In[ ]:


# Write a Python program to check a triangle is equilateral, isosceles or scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.

def check_triangle(side1, side2, side3):
    if side1==side2==side3:
        print('This is an equilateral triangle!')
    elif side1==side2 or side1==side3 or side2==side3:
        print('This is an isosceles triangle!')
    else:
        print('This is a scalene triangle!')

check_triangle(1,2,1)
