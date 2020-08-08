# Day 28 - Problem 32

# Challenge
# Write a Python script to display the various Date Time formats.

from datetime import datetime


# a) Current date and time
current_datetime = datetime.now()
print("Current date and time is: " + str(datetime.now()))
# b) Current year
print("Current year: " + str(current_datetime.year))
# c) Month of year
print("Current month: " + str(current_datetime.month))
# d) Week number of the year
print("Current week: " + str(current_datetime.strftime("%V")))
# e) Weekday of the week
print("Weekday of the week: " + str(current_datetime.weekday() + 1))
# f) Day of year
print("Day of year: " + str(current_datetime.strftime("%j")))
# g) Day of the month
print("Day of month: " + str(current_datetime.strftime("%d")))
# h) Day of week
print("Day of week: " + str(current_datetime.strftime("%A")))
