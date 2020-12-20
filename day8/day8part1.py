
theList = open("day8input.txt","r").read().split('\n')
indexDone = []
accumulator = 0
index = 0

while True:

    if index in indexDone:
        break


    instruction, value = theList[index].split(' ')
    indexDone.append(index)
    if instruction == "acc":
        accumulator += int(value)
        index += 1
    elif instruction == "jmp":
        index += int(value)
    else:
        index += 1



print(accumulator)