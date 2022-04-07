import random

# initial deposit and compounding interest rate
amount = 100
compoundRate = .03

# print the beginning balance
print (("Balance at beginning of month 1: %.2f\n") % amount)
monthCompound = amount * compoundRate
amount += monthCompound

# generate random float between 100 and 500
deposit = random.uniform(100, 501)
# add deposit to balance and print confirmation
amount += deposit
print(("You have deposited: %.2f, thank you\n") % deposit)

# month 2
print(("Balance at beginning of month 2: %.2f\n") % amount)
monthCompound = amount * compoundRate
amount += monthCompound

# month 3
print(("Balance at beginning of month 3: %.2f\n") % amount)
monthCompound = amount * compoundRate
amount += monthCompound

# print final balance
print(("Balance after 3 months: %.2f") % amount)