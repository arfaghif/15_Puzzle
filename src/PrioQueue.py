from puzzle import *
import sys
class PrioQueue:
    def __init__(self,puz):
        if(puz.canSolve()):
            self.elements =[puz]
        else:

            raise Exception("Sum Kurang(I) + X bernilai ganjil sehingga puzzle tidak dapat diselesaikan")
    def isEmpty(self):
        return self.elements ==[]
    def run(self):

        while(not (self.isEmpty())):
            index = 0
            curCost = self.elements[0].getCost()
            for i in range (1, len(self.elements)):
                if (self.elements[i].getCost()<curCost):
                    curCost = self.elements[i].getCost()
                    index = i
            #print(repr(self))
            puzzle1 = self.elements.pop(index)

            if(puzzle1.isSolution()):
                return puzzle1

            if (getattr(puzzle1,'lastDirection') != "left" and puzzle1.getPointerIdx()%4 !=0):
                puzzle2 = puzzle1.nextPuzzle("left")
                if puzzle2.canSolve():
                    self.elements.append(puzzle2)
            if (getattr(puzzle1,'lastDirection') != "right" and puzzle1.getPointerIdx()%4 !=3):
                puzzle2 = puzzle1.nextPuzzle("right")
                if puzzle2.canSolve():
                    self.elements.append(puzzle2)
            if (getattr(puzzle1,'lastDirection') != "up" and puzzle1.getPointerIdx() >= 4):
                puzzle2 = puzzle1.nextPuzzle("up")
                if puzzle2.canSolve():
                    self.elements.append(puzzle2)
            if (getattr(puzzle1,'lastDirection') != "down" and puzzle1.getPointerIdx() < 12):
                puzzle2 = puzzle1.nextPuzzle("down")
                if puzzle2.canSolve():
                    self.elements.append(puzzle2)

    def __repr__(self):
        s= "[ "
        for matriks in self.elements:
            s+=str(getattr(matriks,'id')) + " "
        return s


            
# l=[]
# for i in range(1,17):
#     l.append(i)

# #random.shuffle(l)
#l =[1,2,3,4,5,6,16,8,9,10,7,11,13,14,15,12]
# l=[1,3,4,15,2,16,5,12,7,6,11,14,8,9,10,13]
# l = [1,2,3,4,5,6,16,8,9,10,7,11,13,14,15,12]
# p = Puzzle(l)
# pq = PrioQueue(p)
# pq.run()
# print (repr(p))

# q = p.nextPuzzle("up")
# print (repr(q))

# q.printBranch()