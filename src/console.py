from PrioQueue import *

l = [i for i in range(1,17)]
# with open("../TestCase/Tc03.txt",'r') as file:
#     l=[int(num)  for line in file for num in line.split(" ")]

puzzle = Puzzle(l)
print(puzzle)

s = input("Masukkan console :")
while (s!="end"):
    if(s in ["left","right","up","down"]):
        try:
            puzzle = puzzle.nextPuzzle(s)
            print(puzzle)
        except Exception as error:
            print("Error : " + str(error))
    else:
        print("Typo yaaa ... Hehe")
    s=input("Masukkan console :")
    

