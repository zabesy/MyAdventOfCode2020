
theList = open("day2input.txt").read().split("\n")
values = []
valid = 0

for line in theList:
    total = 0
    values = line.split(' ')
    lower,upper = values[0].split('-')
    character = values[1].replace(':','')
    
    for nr in values[2]:
        if nr == character:
            total=total+1
    
    if total >= (int(lower)) and total <= (int(upper)):
        valid=valid+1
    


print(valid)