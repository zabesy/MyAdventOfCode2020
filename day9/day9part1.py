

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


