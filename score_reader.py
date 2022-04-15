namesList = list()
namesFile = open("score.txt", "r")
numRecords = 0
totalScore = 0
total = 0
classTotal = 0
i = 1
while not namesFile.closed:
    aLine = namesFile.readline().rstrip()
    fields = aLine.split()
    
    
    if aLine != "":
        #namesList.append(aLine)
        #print(fields)
        while i <= len(fields) - 1:
            #print(fields[i])
            totalScore += float(fields[i])
            total = totalScore / (len(fields) - 1)
            i += 1
        print("Total score for " + fields[0] + " = " + str(total) + "%")
        classTotal += total
        numRecords += 1
        total = 0
        totalScore = 0
        i = 1
    else:
        namesFile.close()
    
classAvg = classTotal / numRecords
print("\nTotal number of records: " + str(numRecords))
print(("Class average = %.2f%%") % classAvg)