
theList = open("day2input.txt").read().split("\n")
values = []
valid = 0

for line in theList:
    values = line.split(' ')
    lower,upper = values[0].split('-')
    character = values[1].replace(':','')


    if (values[2][(int(lower)-1)] == character) or (values[2][(int(upper)-1)] == character):
        if (values[2][(int(lower)-1)] == character) and (values[2][(int(upper)-1)] == character):
            continue
        valid=valid+1


print(valid)