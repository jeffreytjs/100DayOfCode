# Day 27 - Problem 30

# Challenge
# Write a Python program to convert Year/Month/Day to Day of Year in Python

from datetime import datetime


# input = input("Type in the YYYY/MM/DD to convert: ")
input = '2020/03/03'
year = input[:4]
input_date = datetime.strptime(input, '%Y/%m/%d').date()
start_yr = datetime.strptime(year + "/01/01", '%Y/%m/%d').date()
day_of_year = (input_date - start_yr).days + 1
print(day_of_year)
