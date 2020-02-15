#!/usr/bin/env python
# coding: utf-8
# Day 12 - Problem 15
# In[ ]:


# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
# Write a Python program that accepts a string and calculate the number of digits and letters
# Sample Data : "Python 3.2"
# Expected Output :
# Letters 6
# Digits 2

def count_digit_letter(string):
    letters = 0
    digits = 0
    for i in string:
        if i.isalpha():
            letters += 1
        elif i.isnumeric():
            digits += 1
    print('Letters ' + str(letters))
    print('Digits ' + str(digits))

string = "Python 3.2"
count_digit_letter(string)
