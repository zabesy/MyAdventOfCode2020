
theList = open("day6input.txt","r").read().split("\n\n")
count = 0
charsDone = []
charToRemove = []
total = 0

for line in theList:
    listan = line.split('\n')

    for char in listan[0]:
        charsDone.append(char)
    

    for string in listan[1:len(listan)]:
        for theChar in charsDone:
            print(theChar)
            if theChar not in string:
                charToRemove.append(theChar)
     
    
    for char in charToRemove:
        if char in charsDone:
            charsDone.remove(char)
            
    total += len(charsDone)

    charToRemove = []
    charsDone = []
    
print(total)
