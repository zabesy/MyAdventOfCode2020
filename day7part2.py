
def recur(val):
    global total
    global recursedStrings
    for values in newDict:
        for values2 in newDict[values]:
            if (val in values2) and (val not in recursedStrings):
                print(values2)
                total += int(list(values2.values())[0])
                recursedStrings.append(values2)
                recur(values2)
                

theList = open("day7input.txt","r").read().split('\n')
total = 0

recursedStrings = []

newDict = {}
for line in theList:
    stringArray = line.split(' ')

    if len(stringArray) == 7:
        continue

    for i in range(4, len(stringArray),4):
        newDict.setdefault((stringArray[0] + " " + stringArray[1]),[]).append({((stringArray[i+1] + " " + stringArray[i+2])):stringArray[i]})



for values in newDict:
    for values2 in newDict[values]:
        if "shiny gold" in values2:
            recur(list(values2)[0])
            total += int(list(values2.values())[0])

print(total)
