
lines = []
theList = open("day8input.txt").read().split('\n')
for each in theList:
    each = each.rstrip().split(' ')
    lines.append([each[0], int(each[1])])



def test(lines):

    checked = set()
    accumulator = 0
    index = 0
    while True:
        if index >= len(lines):
            return accumulator
        instruction, value = lines[index]
        if index in checked:
            return False
        checked.add(index)

        if instruction == "acc":
            index += 1
            accumulator += value
        elif instruction == "jmp":
            index += value
        else:
            index += 1


for index, line in enumerate(lines):
    if line[0] == "nop" or line[0] == "jmp":
        prev = line[0]
        lines[index][0] = "jmp" if line[0] == "nop" else "nop"
        if accumulator:= test(lines):
            break
        lines[index][0] = prev


print(accumulator)




