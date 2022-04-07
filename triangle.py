# Given a right triangle write a python script to compute the lengths
# of side a and b given the angle ang = 30 degrees and the hypotenuse (c) = 11

# import math module
import math

# the given angle and hypotenuse length
angle = 30
hypotenuse = 11

# A = Hypotenuse x sine(angle) - convert 30 degree angle to radians
sideA = hypotenuse * math.sin(math.radians(angle))
# B = Hypotenuse x cosine(angle) - convert 30 degree angle to radians
sideB = hypotenuse * math.cos(math.radians(angle))

# print both sides
print(("Side A of the right triangle is: %.1f") % sideA)
print(("Side B of the right traingle is: %.11f") % sideB)