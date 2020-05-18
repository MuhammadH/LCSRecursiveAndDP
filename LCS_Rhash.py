

'''
This script will create a simple custom hash map and use
the number of LCS recursions from LCSRec for each value
as a key.

The hash map is then graphed to show how many collisions
occured in the hash map. 
'''

# picked 5000 as the limit


import time
import plotly.graph_objects as go

class RecsAndLen:
    recCalls = 0
    lcsNum = 0

class MyHashTable:
    chains = []
    def __init__(self):
        for i in range(10000): # originally 1000000
            newChain = []
            self.chains.append(newChain)
    def addThis(self, ral, actNum):
        if ral.recCalls > 5000:
            ral.recCalls %= 5000
        self.chains[ral.recCalls].append(actNum)


def LCSRec(str1, str2, place1, place2):
    lcsInt = 0
    recInt = 0
    ral = RecsAndLen()
    
    if place1 > len(str1) - 1:
        ral.recCalls = 0
        ral.lcsNum = 0
        return ral
    if place2 > len(str2) - 1:
        ral.recCalls = 0
        ral.lcsNum = 0
        return ral
    
    if str1[place1] == str2[place2]:
        nextCall = LCSRec(str1, str2, place1 + 1, place2 + 1)
        
        lcsInt = 1 + nextCall.lcsNum
        recInt = 1 + nextCall.recCalls
    else:
        check1 = LCSRec(str1, str2, place1 + 1, place2)
        check2 = LCSRec(str1, str2, place1, place2 + 1)
        lcsInt = max(check1.lcsNum, check2.lcsNum)
        recInt = 1 + check1.recCalls + check2.recCalls
    
    ral.recCalls = recInt;
    ral.lcsNum = lcsInt;
    return ral
    
    return lcsInt;

# make list
fullList = []
s = 100000
for i in range(9000): # orignally 900000
    fullList.append(s)
    s += 1

# string for comparison
strc = "0123456789"

# make hash table
mht = MyHashTable()

# get hashes and add to hash table
for i in fullList:
    actNum = i
    ral = LCSRec(strc, str(i), 0, 0)
    mht.addThis(ral, actNum)

# print graph
yset = []
xset = []
counter = 0;
for i in mht.chains:
    if len(i) > 0:
        yset.append(len(i))
        xset.append(counter)
    counter += 1

fig = go.Figure(data=go.Bar(x=xset, y=yset))
fig.show()


