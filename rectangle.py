#!/usr/bin/python

# create class Rectangle
class Rectangle(object):
    # set protected variables
    _length = 0
    _width = 0
    
    # create constructor method that takes length and width parameters
    def __init__(self, length, width):
        self._length = length
        self._width = width
        
    # method that returns the area of the rectangle object    
    def getArea(self):
        # A = L x W
        area = self._length * self._width
        return area
    
    # if the length = the width, we have a square
    def isSquare(self):
        if self._length == self._width:
            return True
        else:
            return false
    
    # equivalence overload to compare length and width of two rectangles
    def __eq__(self, other):
        if self._length == other._length and self._width == other._width:
            return True
        
# This code tests the functionality of your Rectangle class (provided by instructor)
if __name__ == '__main__':
    rect1 = Rectangle(10,10)
    rect2 = Rectangle(10,10)
    rect3 = Rectangle(10,15)
    if rect1 == rect2:
        print("Test 1 pass")
    if rect1.isSquare():
        print("Test 2 pass")
    if rect3 == rect1:
        print("Test 3 FAIL")
    else:
        print("Test 3 pass")
        
    # added test to ensure that getArea method is functioning properly (provided by Jeremy)
    print(rect1.getArea())