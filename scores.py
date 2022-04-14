#!/usr/bin/python

# initialize the average to 0
avg = 0

# get the 3 scores from user in 98/100 format
total1 = input("Enter the first score (xx/100 format): ").split("/")
total2 = input("Enter the second score (xx/100 format): ").split("/")
total3 = input("Enter the third score (xx/100 format): ").split("/")

# store the scores (numerator) for each test
score1 = float(total1[0])
score2 = float(total2[0])
score3 = float(total3[0])

# score the total possible points (denominator) per test
maxScore1 = int(total1[1])
maxScore2 = int(total2[1])
maxScore3 = int(total3[1])

# calculate the avergae score
avg = ((score1 + score2 + score3) / (maxScore1 + maxScore2 + maxScore3) * 100)

# print the average
print(("\nYour average was: %.2f") % avg)

# if the average is above 95%, print the message
if avg > 95:
    print("\nGreat work! Your average was over 95%!")

# if less than 95, print message
else:
    print("\nKeep studying!")