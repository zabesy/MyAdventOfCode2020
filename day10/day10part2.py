def numOfValid(number):
    #number of valid next numbers, return their values
    global theList
    #find index of number
    index = theList.index(number)
    hejsan = []

    lengthDiff = len(theList) - index
    if lengthDiff <= 3:
        for g in range(index+1,len(theList)):
            if theList[g] - theList[index] <= 3:
                hejsan.append(theList[g])
    else:
        for g in range(index+1,index+4):
            if theList[g] - theList[index] <= 3:
                hejsan.append(theList[g])


    return hejsan

def recur(num):
    global mult
    global theList
    mult *= 2**(len(numOfValid(num))-1) # if len(numOfValid(num)) > 1 else 1

    #return the numbers that are valid

    #print(numOfValid(num)[0] if len(numOfValid(num)) != 0 else None)

    if len(numOfValid(num)) != 0:
        recur(numOfValid(num)[0])

    #for number in numOfValid(num):
    #    recur(number)
        #because when we come here we've already searched for all solutions
    #    break

    return mult




theList = []

for line in open("testinput.txt").read().split('\n'):
    theList.append(int(line))


index = 0
changed = False


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

number = theList[len(theList)-1]
theList.append(number+3)
theList.insert(0,0)

print(theList)
mult = 1
print(recur(0))






