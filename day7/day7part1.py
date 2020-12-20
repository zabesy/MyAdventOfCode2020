
def recur(val):
    global total
    global recursedStrings
    for values in newDict:
        if (val in newDict[values]) and (values not in recursedStrings) :
            total += 1
            recursedStrings.append(values)
            recur(values)


theList = open("day7input.txt","r").read().split('\n')
total = 0
recursedStrings = []

newDict = {}
for line in theList:
    stringArray = line.split(' ')

    if len(stringArray) == 7:
        continue

    for i in range(5, len(stringArray),4):
        newDict.setdefault((stringArray[0] + " " + stringArray[1]),[]).append(stringArray[i] + " " + stringArray[i+1])
   
for values in newDict:
    if "shiny gold" in newDict[values]:
        recur(values)
        total += 1

print(total)
    #newDict[str(stringArray[0] + " " + stringArray[1])] =
