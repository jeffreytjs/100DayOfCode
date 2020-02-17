#!/usr/bin/env python
# coding: utf-8
# Day 15 - Problem 18
# In[ ]:


# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
import random
def guessing_game(input):
    answer = random.randrange(1,9)
    guess = int(input("Guess a number between 1 and 9: "))
    while guess != answer:
        if guess < answer:
            guess = int(input("Too low, try a higher number: "))
        else:
            guess = int(input("Too high, try a lower number: "))
    print("Your guess is right!")

guessing_game(input)
