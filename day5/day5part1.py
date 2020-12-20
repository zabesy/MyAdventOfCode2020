
theList = open("day5input.txt","r").read().split('\n')

listOfIDs = []
highestID = 0
rowInterval = [0,128]
colInterval = [0,8]
row = 128
col = 8


for line in theList:
    
    rowInterval = [0,128]
    colInterval = [0,8]
    row = 128
    col = 8

    for char in line:
        if char == 'F':
            row = row/2
            rowInterval[1] = rowInterval[0]+row
        elif char == 'B':
            row = row/2
            rowInterval[0] = rowInterval[1]-row
        
        if char == 'L':
            col = col/2
            colInterval[1] = colInterval[0]+col
        elif char == 'R':
            col = col/2
            colInterval[0] = colInterval[1]-col
        
    num = rowInterval[0]*8 + colInterval[0]


    highestID = num if (num > highestID) else highestID


print(highestID)
