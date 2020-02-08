#!/usr/bin/env python
# coding: utf-8
# Day 7 - Problem 10
# In[2]:


#  Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700

def find_num(start, end, div, mul):
    numbers = []
    for i in list(range(start, end+1)):
        if (i % div == 0 and i % mul == 0):
            numbers.append(i)
    print("Numbers divisible by " + str(div) + " and multiple of " + str(mul) + ": " + str(numbers).strip('[]'))

find_num(1500, 2700, 7, 5)
