# Day 28 - Problem 34

# Challenge
# Write a Python program to subtract five days from current date

from datetime import datetime, timedelta


days_to_subtract = 5
d = datetime.today() - timedelta(days=days_to_subtract)
