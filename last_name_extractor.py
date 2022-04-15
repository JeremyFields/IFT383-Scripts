#!/usr/bin/python

# prompt user for full name
fullName = input("Please enter your full name: ")

# function to extract the first name
def firstName (fullName):
    # set firstName = the full name, split at the space
    # and thus the first index will be the first name
    firstName = fullName.split(" ")[0]
    return firstName
    
# main function used to call the firstName function
def main():
    # print first name by calling firstName function and passing
    # the fullName received from user
    print( "Hello " + firstName(fullName) + "!" )
    
# if run from the terminal, execute main automatically
if __name__ == "__main__":
    main()