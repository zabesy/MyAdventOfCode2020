
inputString = open("firstInput.txt").read().split("\n")
inputInt = [int(every) for every in inputString] 

for i in range(len(inputInt)):
    for j in range(i+1,len(inputInt)):
        if(inputInt[i] + inputInt[j] == 2020):
            print("i = " + str(i) + "\n" + "j = " + str(j))
            print("WE GOT IT!!" + "\n" + str(inputInt[i] * inputInt[j]))
            break