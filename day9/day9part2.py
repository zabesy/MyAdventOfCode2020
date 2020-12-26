
def findMaxMin(first,last):
    global theList
    smallest = theList[first]
    largest = 0
    for num in range(first,last+1):
        if theList[num] < smallest:
            smallest = theList[num]
        if theList[num] > largest:
            largest = theList[num]
    return smallest + largest



theList = []

for line in open("day9input.txt").read().split('\n'):
    theList.append(int(line))

preamble = 25
solution = False

while True:
    #0-24
    for i in range(preamble-25, preamble-1):
        #i(1-25)-25

        for j in range(i+1,preamble):
            if theList[i]+theList[j] == theList[preamble]:
                #then it has a solution
                solution = True

    if not solution:
        print(theList[preamble])
        break

    preamble += 1
    solution = False

invalidNumber = theList[preamble]
newList = []

#find the list of numbers that sums up to invalid number
while True:
    for i in range(len(theList)-1):
        if theList[i] == invalidNumber:
            continue
        sum = theList[i]

        for j in range(i+1,len(theList)):
            if theList[j] == invalidNumber:
                continue

            sum += theList[j]

            #then it has gone too far, restart from theList[i]
            if sum > invalidNumber:
                break
            elif sum == invalidNumber:
                #if sum is found, save the index of i and j
                #findMaxMin(i,j)
                print(findMaxMin(i,j))
                exit()





