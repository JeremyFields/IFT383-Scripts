#!/usr/bin/python

# function to calculate score data
def scores(namesFile):
    # initialize needed local variables
    numRecords = 0
    totalScore = 0
    total = 0
    classTotal = 0
    i = 1
    
    # while file is open
    while not namesFile.closed:
        # read each line
        aLine = namesFile.readline().rstrip()
        # split the line into fields
        fields = aLine.split()
        
        # if the line is not empty (data still remains)
        if aLine != "":
            # loop to stay inside index boundaries of fields
            while i <= len(fields) - 1:
                # calculate the total score by adding up test values
                totalScore += float(fields[i])
                # calculate the final score / average for each student
                total = totalScore / (len(fields) - 1)
                # increase i to iterate the loop
                i += 1
            
            # print the final score for each student
            print("Total score for " + fields[0] + " = " + str(total) + "%")
            # calculate the total score of the class
            classTotal += total
            # increase the number of records each time we loop through a line
            numRecords += 1
            # reset values for the next file loop through
            total = 0
            totalScore = 0
            i = 1
        # once no data left, close file
        else:
            namesFile.close()
    
    # calculate the class average
    classAvg = classTotal / numRecords
    
    # return the number of records and class average
    return numRecords, classAvg

# main function to open file, call scores function and pass the file
def main():
    # read in the file
    namesFile = open("score.txt", "r")
    # get the returned values from the scores function
    values = ( scores(namesFile) )
    # print the number of records and class average
    print(("\nNumber of records: %i") % values[0])
    print(("Class Average = %.2f%%") % values[1])
    
# run the main function if script is run from command line
if __name__ == "__main__":
    main()