
theList = open("day6input.txt","r").read().split("\n\n")
count = 0
charsDone = []
total = 0

for line in theList:
    listan = line.split('\n')

    for string in listan:
        for char in string:
            if char not in charsDone:
                charsDone.append(char)
    
    total += len(charsDone)

    charsDone = []
    
print(total)

        
        