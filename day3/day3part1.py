
listan = open("day3input.txt").read().split('\n')
tree = 0
row=0
col=3
character = '#'

for row in range(1,len(listan)):

    if col >= len(listan[row]):
        col-=(len(listan[row]))


    if listan[row][col] == str(character):
        tree+=1

    col+=3

print(tree)

