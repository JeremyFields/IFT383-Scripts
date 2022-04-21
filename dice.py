#!/usr/bin/python

# import random module
import random

# your class definition goes here
class Die(object):
    
    # contructor method for creating die object with number of sides provided
    def __init__(self, sides=0):
        if type(sides) is int:
            self._sides = sides
        else:
            print("Please enter an integer reflecting how many sides the die has.")
    
    # roll method to roll random int between 1 and number of sides
    def roll(self):
        return random.randint(1, self._sides)
    
    # roll multiple method that is passed the number of times to roll,
    # and continues rolling, appending the number to the list rollList
    def rollMultiple(self, number):
        i = 0
        # list to store each roll value
        rollList = []
        while number > i:
            rollList.append(random.randint(1,6))
            i += 1
        return rollList
    
    # get sides method that returns the number of sides the die has
    def getSides(self):
        return self._sides
        
        
# testing code
# please do not edit
myd = Die(6)
md = myd.rollMultiple(1000)
if type(myd.roll()) is int:
    print("test 1 pass")
if len(md) == 1000:
    print("test 2 pass")
if max(md) == 6:
    print("test 3 pass")
if min(md) == 1:
    print("test 4 pass")
if myd.getSides() == 6:
    print("test 5 pass")