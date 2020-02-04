#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

user_name = input("Please enter your name: ")
user_age = input("Please enter your age: ")
year = (2020-int(user_age)+100)
print("Hi " + user_name + ", you will turn 100 years old in the year " + str(year) + "!")
