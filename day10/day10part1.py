
theList = []

for line in open("day10input.txt").read().split('\n'):
    theList.append(int(line))


index = 0
changed = False

sortedList = []

for i in range(len(theList)):
    changed = False
    smallest = theList[i]
    for j in range(i+1,len(theList)):
        if theList[j] < smallest:
            changed = True
            smallest = theList[j]
            index = j

    if changed:
        theList.pop(index)
        theList.insert(i,smallest)

numberOf3s = 1
numberOf1s = 1
continousList = []
listan = []
print(theList)

for num in range(len(theList)):
    diff = theList[num]-theList[num-1]
    if diff > 3:
        listan.append(continousList)
        continousList = []
        break
    elif diff == 3:
        numberOf3s += 1
    elif diff == 1:
        numberOf1s += 1
    continousList.append(theList[num-1])



print(numberOf1s*numberOf3s)



