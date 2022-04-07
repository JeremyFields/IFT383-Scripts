#!/usr/bin/python

# Lab 5 - IFT383
# Part2-jbfields.py

# import math module
import math

# gather user input for the x and y coordinates of
# both points and split them with a ", "
x1, y1 = input("Enter x1 and y1 for Point 1: ").split(", ")
x2, y2 = input("Enter x2 and y2 for Point 2: ").split(", ")


# calculate delta X and delta Y
deltaX = float(x2) - float(x1)
deltaY = float(y2) - float(y1)

# calculate the distance between the two points and round to one decimal place
distance = round(math.sqrt(pow(deltaX, 2) + pow(deltaY, 2)), 1)

# print the results
print(("The distance between (%s, %s) and (%s, %s) is %.1f") % (x1, y1, x2, y2, distance))
