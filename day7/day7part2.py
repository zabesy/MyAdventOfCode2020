def recur(val):
    total = 0
    for value in newDict[val]:
        if value is not None:
            ret = recur(value[0])
            total += ret * value[1]
        else:
            total += 1
    return total


theList = open("day7input.txt", "r").read().split('\n')
total = 0

newDict = {}

for line in theList:
    stringArray = line.split(' ')

    if len(stringArray) == 7:
        newDict.setdefault((stringArray[0] + " " + stringArray[1]), []).append(None)
        continue

    for i in range(4, len(stringArray), 4):
        newList = [(stringArray[i + 1] + " " + stringArray[i + 2]), int(stringArray[i])]
        newDict.setdefault((stringArray[0] + " " + stringArray[1]), []).append(newList)


for value in newDict["shiny gold"]:
    ret = recur(value[0])
    total += ret * value[1]

print(total)
