
import time

def LCSRec(str1, str2, place1, place2):
    if place1 > len(str1) - 1:
        return 0
    if place2 > len(str2) - 1:
        return 0
    
    if str1[place1] == str2[place2]:
        return 1 + LCSRec(str1, str2, place1 + 1, place2 + 1)
    else:
        check1 = LCSRec(str1, str2, place1 + 1, place2)
        check2 = LCSRec(str1, str2, place1, place2 + 1)
        return max(check1, check2)



# make empty list
numList = []

# get and open file
fileName = "randNums.txt"
numFile = open(fileName, 'r')

# read file
lines = numFile.read()

# split file and add each number to a list
linesSplit = lines.split()
for i in linesSplit:
    numList.append(int(i))

# remember to close file
numFile.close()

# string for comparison
str1 = "0123456789"

# timer
timeStart = time.time()

# run for each int
for i in numList:
    val = LCSRec(str1, str(i), 0, 0)

timeEnd = time.time()
print ("total run time:", timeEnd - timeStart)


