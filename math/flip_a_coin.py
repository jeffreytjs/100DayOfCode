# Day 50 - Problem 56

# Challenge
# Write a Python program to flip a coin 1000 times and count heads and tails.


import random


def coin_flips(n):
    flip_count = {
        'heads': 0,
        'tails': 0
    }
    for i in range(n):
        if random.randint(0, 1) == 0:
            flip_count['heads'] += 1
        else:
            flip_count['tails'] += 1

    return flip_count


n = 1000
print(coin_flips(n))
