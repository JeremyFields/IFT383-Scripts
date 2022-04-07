#!/usr/bin/python

# get input from user
userInput = input("Please enter some number of seconds: ")

# evaluate as integer for use in expressions
userInput = eval(userInput)

# set constant for number of seconds / hour
SECS_PER_HOUR = 3600

# calculate hours
hours = userInput / SECS_PER_HOUR
numHours = int(hours)

# calculate remaining minutes after rouding off (see above)
mins = hours - numHours
numMins = int(mins * 60)

# print the output
print(userInput, "seconds is equivalent to", numHours, "hour and", numMins, "minutes.")