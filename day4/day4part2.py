
def birthYear(byr):
    return (int(byr) >= 1920) and (int(byr) <= 2002) 

def issueYear(iyr):
    return (int(iyr) >= 2010) and (int(iyr) <= 2020) 

def expireYear(eyr):
    return (int(eyr) >= 2020) and (int(eyr) <= 2030)

def height(hgt):
    if "cm" in hgt:
        number = hgt.replace("cm","")
        return int(number) >= 150 and int(number) <= 193
    elif "in" in hgt:
        number = hgt.replace("in","")
        return int(number) >= 59 and int(number) <= 76
    return False

def hairColor(hcl):
    if hcl[0] == '#':
        for char in range(1,len(hgt)):
            if ((hcl[char] >= '0') and (hcl[char] <= '9')) or ((hcl[char] >= 'a') and (hcl[char] <= 'f')):
            #if ((ord(hcl[char]) >= ord('0')) and (ord(hcl[char]) <= ord('9'))) or ((ord(hcl[char]) >= ord('a')) and (ord(hcl[char]) <= ord('f'))):
                continue
            return False
        return True
    return False

def eyeColor(ecl):
    eyeColors = ["amb","blu","brn","gry","grn","hzl","oth"]
    if ecl in eyeColors:
        return True
    return False

def passportId(pid):
    if len(pid) == 9:
        return True
    return False


theList = open("day4input.txt").read().split("\n\n")
newDict = {}
fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
valid = 0

for line in theList:
    newDict = {}
    idk = line.replace('\n',' ').split(' ')
    
    for each in idk:
        each = each.split(':')
        newDict[each[0]] = each[1]
    
    #Checks if all keys in the dict contains in the fields list
    if all(key in newDict.keys() for key in fields):
        byr = newDict[fields[0]]
        iyr = newDict[fields[1]]
        eyr = newDict[fields[2]]
        hgt = newDict[fields[3]]
        hcl = newDict[fields[4]]
        ecl = newDict[fields[5]]
        pid = newDict[fields[6]]
        
        print(hairColor(hcl))

        if birthYear(byr) and issueYear(iyr) and expireYear(eyr) and height(hgt) and hairColor(hcl) and eyeColor(ecl) and passportId(pid):
            valid += 1

print(valid)

    