
listan = open("day3input.txt").read().split('\n')
tree = 0
totaltrees = 1
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
character = '#'
col = 0
row = 0

for iteration in range(len(slopes)):

    for row in range(slopes[iteration][1],len(listan),slopes[iteration][1]):
        
        col+=slopes[iteration][0]

        col %= len(listan[row])

        if listan[row][col] == str(character):
            tree+=1

    totaltrees *= tree
    tree = 0
    col = 0
    row = 0


print(totaltrees)



