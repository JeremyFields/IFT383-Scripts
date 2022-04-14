#!/usr/bin/python

# set annual rate to 4%
annRate = .04

# prompt user for the initial deposit amount
initDeposit =  int(input("Please enter the starting balance: "))
# set years = 0, as the starting point
years = 0

# loop while the balance is less than $1,000,000
while initDeposit < 1000000:
    # calculate the interest accrued in first year
    interest = initDeposit * annRate
    # update the balance to the interest accrued + the initial balance
    initDeposit = initDeposit + interest
    # add one year each time it loops
    years += 1
    
# change the decimal interest rate to the actual percentage
annRate = annRate * 100

# print the statement, in how many years will it take to acquire $1,000,000
print(("\nIn %i years at %i%% compounded interest, you will be a millionaire!") % (years, annRate))