#!/usr/bin/python
import math

# ==========================================================================

# parent Account class
class Account(object):
    # protected class variables
    _name = ""
    _balance = 0.0
    _transactionCounter = 0
    
    # constructor method for Account objects
    def __init__(self, name="blank", balance=0.0):
        self._name = name
        self._balance = balance
    
    # deposit method to calculate balance upon depositing cash
    def deposit(self, deposit=0.0):
        self._balance += deposit
        self._transactionCounter += 1
        return self._balance
    
    # withdraw method to calculate balance upon withdrawing cash
    def withdraw(self, withdraw=0.0):
        if self._balance > withdraw:
            self._balance -= withdraw
            self._transactionCounter += 1
            return self._balance
        else:
            return False
    
    # overloaded len method to check the amount of transactions
    def __len__(self):
        return self._transactionCounter
    
    # overloaded str method to check the account holders name
    def __str__(self):
        return self._name
    
    # overloaded equality method to check the balances of two accounts
    def __eq__(self, other):
        if self._balance == other._balance:
            return True
        else:
            return False

# child CreditAccount class
class CreditAccount(Account):
    # private class variables
    __limit = 0.0
    __rate = 0.0
    
    # overriden constructor method for CreditAccount objects
    def __init__(self, name="blank"):
        self._name = name
        self._balance = 0.0
        self.__limit = 1000.0
        self.__rate = 1.24
    
    # deposit method to deposit cash to pay down credit balance
    def deposit(self, deposit=0.0):
        self._balance -= deposit
        if self._balance < 0.0:
            self._balance = 0.0
        return self._balance
    
    # withdraw method that calculates the charge multiplied by the rate
    def withdraw(self, withdraw=0.0):
        # if current balance + charge is less than the credit limit
        # allow the transactiont to proceed and update balance
        if self._balance + withdraw < self.__limit:
            self._balance += withdraw * self.__rate
            self._transactionCounter += 1
            return self._balance
        # if greater than or equal to the credit limit, return false
        elif self._balance + withdraw >= self.__limit:
            return False

# child SavingsAccount class
class SavingsAccount(Account):
    # inherit constructor from parent Account class
    pass
    
    # calculate deposit and bonus on deposit
    def deposit(self, deposit=0.0):
        self._balance = deposit * 1.413
        self._transactionCounter += 1
        return self._balance
    
    # calculate interest accrual
    def accrue(self):
        self._balance *= 1.05
        return self._balance

# ==========================================================================

## DO NOT MODIFY BEYOND THIS POINT!
## Submissions with modifications beyond this line will be given a 0 score
## We will check... we have the technology :-)
if __name__ == "__main__":
    myScore = 0

    # Test base account
    acct = Account('Chelsey', 1024.32)

    # test withdraw method overdraft
    if acct.withdraw(100000.00) == False:
        myScore += 5
    else:
        print("ERROR: Account.withdraw(ammount) did not return False.")

    # Test withdraw method balance OK
    if acct.withdraw(60.01) == 964.31:
        myScore += 5
    else:
        print("ERROR: Value returned when attempting to make a withdrawal was unexpected")

    # test deposit function
    if acct.deposit(36.50) == 1000.81:
        myScore += 5
    else:
        print("ERROR: The deposit function on Account class returned an unexpected value")

    # test transaction counter
    if len(acct) == 2:
        myScore += 5
    else:
        print("ERROR: The transaction counter returned an unexpected result when using len()")

    # Check toString()
    if str(acct) == 'Chelsey':
        myScore += 5
    else:
        print("ERROR: Converting Account to a string had an unexpected resule")

    # Test equivilance operator
    acct2 = Account('Sam', 1000.81)
    if acct == acct2:
        myScore += 5
    else:
        print("ERROR: Equivilance op test #1 failed")
    acct2.withdraw(1000.00)
    if acct == acct2:
        print("ERROR: Equivilance op test #2 failed")
    else:
        myScore += 5

    # Test the CreditAccount class
    acct = CreditAccount('Chelsey')

    # Test inherited methods
    if str(acct) == 'Chelsey':
        myScore += 5
    else:
        print("ERROR: When testing inherited methods for CreditAccount")
    
    # Test withdraw function
    if acct.withdraw(100000.00) == False:
        myScore += 5
    else:
        print("ERROR: CreditAccount.withdraw did not return expected false")
    if acct.withdraw(100.00) == 124.00:
        myScore += 5
    else:
        print("ERROR: CreditAccount.withdraw returned unexpected result")

    # test deposit function
    if acct.deposit(100.00) == 24.00:
        myScore += 5
    else:
        print("ERROR: CreditAccount.deposit returned unexpected result")
    
    # test transaction counter
    if len(acct) == 1:
        myScore += 5
    else:
        print("ERROR: CreditAccount length was incorrect")

    # test SavingsAccount
    acct1 = SavingsAccount('Hannah', 36.30)
    acct2 = SavingsAccount('Andrew', 156.33)
    if acct1.deposit(100.00) == 141.30:
        myScore += 5
    else:
        print("ERROR: deposit for savings account had unexpected return")

    # test accrue
    if acct1.accrue() == 148.365:
        myScore += 5
    else:
        print("ERROR: deposit for savings account had unexpected return")
print ("Grading complete: your score is %d out of 70" % (myScore) )