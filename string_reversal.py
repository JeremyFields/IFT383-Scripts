#!/usr/bin/python

# promp the user for word
string = input("Please enter a word to reverse: ")

# initialize the reversed string
reverse = ""

# set i var to the length of the string minus 1 for the last index
i = len(string) - 1
# loop through the string
for index in string:
    # add the letter from the string at the index i
    # which is the last index for the first iteration
    reverse += string[i]
    # subtract 1 from i to move to the second to last index and
    # continue moving down to the first index
    i -= 1
    
# print the original string and the reversed string
print(("The reverse of %s is %s") % (string, reverse))
