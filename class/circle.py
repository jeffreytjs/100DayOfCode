# Day 20 - Problem 23

# Challenge
# Write a Python class named Circle constructed by a radius
# and two methods which will compute the area and the perimeter of a circle.

import math


class Circle:
    def compute_area(self, radius):
        return math.pi * (radius ** 2)

    def compute_parimeter(self, radius):
        return 2 * math.pi * radius


circle = Circle()
print(circle.compute_area(10))
print(circle.compute_parimeter(10))
