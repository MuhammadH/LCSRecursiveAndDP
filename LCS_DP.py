
import time

def LCSDP(str1, str2, place1, place2, md):
    if place1 > len(str1) - 1:
        return 0
    if place2 > len(str2) - 1:
        return 0
    
    if md[place1][place2] != -1:
        return md[place1][place2]
        
    totalNum = 0
    
    if str1[place1] == str2[place2]:
         totalNum = 1 + LCSDP(str1, str2, place1 + 1, place2 + 1, md)
    else:
        check1 = LCSDP(str1, str2, place1 + 1, place2, md)
        check2 = LCSDP(str1, str2, place1, place2 + 1, md)
        totalNum = max(check1, check2)
        
    md[place1][place2] = totalNum
    return totalNum



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
    md = [[-1 for x in range(10)] for x in range(10)]
    val = LCSDP(str1, str(i), 0, 0, md)

timeEnd = time.time()
print ("total run time:", timeEnd - timeStart)

