# Day 3 - Problem 5

# Challenge
# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them
# the year that they will turn 100 years old.


user_name = input("Please enter your name: ")
user_age = input("Please enter your age: ")
year = (2020 - int(user_age) + 100)


print("Hi " + user_name + ", you will be 100 years old in " + str(year) + "!")
