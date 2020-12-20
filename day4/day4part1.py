
theList = open("day4input.txt").read().split("\n\n")
newDict = {}
fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
valid = 0

for line in theList:
    idk = line.replace('\n',' ').split(' ')
    
    for each in idk:
        each = each.split(':')
        newDict[each[0]] = each[1]
    
    #Checks if all keys in the dict contains in the fields list
    if all(key in newDict.keys() for key in fields):
        valid += 1
        print(valid)

    newDict = {}