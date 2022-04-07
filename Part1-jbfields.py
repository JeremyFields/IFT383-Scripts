#!/usr/bin/python

# Lab 5 - IFT383
# Part1-jbfields.py

# get user input
money = float(input("Enter an amount of money: "))

# cut off cents and store as even number of dollars
numDollars = int(money)
# calculate remainder after subtracting number of even dollars
remainder = money - numDollars
# calculate how many quarters the remainder is divisible by
numQuarters = remainder / 0.25
# subtract the value of a quarter multiplied by quantity of quarters to reduce remainder accordingly
remainder -= (0.25 * int(numQuarters))

# calculate how many dimes the remainder is divible by
numDimes = remainder / 0.10
# subtract the value of a dime multiplied by that quantity of dimes to reduce remainder accordingly
remainder -= (0.10 * int(numDimes))

# calculate how many nickels the remainder is divisible by
numNickels = remainder / 0.05
# subtract the value of a nickel multiplied by that quantity of nickels to reduce remainder accordingly
remainder -= (0.05 * int(numNickels))

# calculate how many pennies the remainder is divisible by
numPennies = remainder / 0.01
# subtract the value of a penny multiplied by that quantity of pennies to reduce remainder accordingly
remainder -= (0.01 * int(numPennies))

# print the results
print(("Your amount %.2f consists of;\n\t %i dollars\n\t %i quarters\n\t %i dimes\n\t %i nickels \n\t %i pennies") \
      % (money, numDollars, numQuarters, numDimes, numNickels, numPennies))