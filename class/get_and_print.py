# Day 24 - Problem 27

# Challenge
# Write a Python class which has two methods get_String and print_String.
# Hint:
# Write a get_String function accepts a string from the user
# Write a print_String function to print the string in upper case


class Process_String:
    def get_String(self):
        self.input = input("Please key in a string: ")

    def print_String(self):
        print(self.input.upper())


process = Process_String()
process.get_String()
process.print_String()
