#!/usr/bin/python

# function to determine if string is a palindrome
def isPalindrome(string):
    # convert passed string to all lowercase so Dad,
    # etc. will not cause incorrect answer
    string = string.lower()
    
    # set variable for the lower index and variable for the upper index
    i = 0
    j = len(string) - 1
    
    # while lower is less than upper, loop
    while i < j:
        # if the string at lower index does NOT equal string
        # at upper index (i.e. if they do not match), return false
        if string[i] != string[j]:
            return False
        
        # increase lower index, decrease upper to move down the
        # string from the beginning and the end simultaneously
        i += 1
        j -= 1
    # if exit loop and have yet to return false, they must all
    # match, so return true
    return True
        
# main function to call the isPalindrome function
def main():
    # promp user for string
    string = input("Enter a string: ")
    # if returned true, print "is a palindrome"
    if isPalindrome(string) == True:
        print(("%s is a palindrome") % string)
    # if returned false, print "is not a palindrome"
    else:
        print(("%s is not a palindrome") % string)

# if run from the command line, run the main function
if __name__ == "__main__":
    main()