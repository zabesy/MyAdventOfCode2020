
def recur(val):
    global total
    global recursedStrings
    for values in newDict:
        if values not in recursedStrings:
            for values2 in newDict[values]:
                if values2 is None:
                    continue
                if val == values2[0]:
                    recur(values2)
                    total *= values2[1]
            recursedStrings.append(values)

                    
            

theList = open("day7input.txt","r").read().split('\n')
total = 1
actualTotal = 0
iteration = 0

recursedStrings = []

newDict = {}
for line in theList:
    stringArray = line.split(' ')

    if len(stringArray) == 7:
        newDict.setdefault((stringArray[0] + " " + stringArray[1]),[]).append(None)
        continue

    for i in range(4, len(stringArray),4):
        newList = [(stringArray[i+1] + " " + stringArray[i+2]),int(stringArray[i])]
        newDict.setdefault((stringArray[0] + " " + stringArray[1]),[]).append(newList)


for values in newDict:
    for values2 in newDict[values]:
        if values2 is None:
            continue
        if "shiny gold" == values2[0]:
            recur(values)
            total *= values2[1]
            recursedStrings = []

print(total)