import copy
import random

class Puzzle:
    countPuzzle = 0
    def __init__(self, mat=None):
        Puzzle.countPuzzle +=1
        self.id = Puzzle.countPuzzle
        self.matriks =   mat
        self.f=0
        self.lastDirection=None
        self.before=None

    
    def nextPuzzle(self, direction):
        p = Puzzle()
        p.f = self.f + 1
        l = self.matriks.copy()
        idx = l.index(16)
        p.before = self
        if (direction=="left"):
            p.lastDirection = "right"
            if(self.getPointerIdx()%4 ==0):
                raise Exception("Mentoookkkkk")
            l[idx] , l[idx-1] = l[idx-1] , l[idx]
        elif (direction == "right"):
            p.lastDirection = "left"   
            if(self.getPointerIdx()%4 ==3):
                raise Exception("Mentoookkkkk") 
            l[idx] , l[idx+1] = l[idx+1] , l[idx]
        elif (direction == "up"):
            p.lastDirection = "down"
            if(self.getPointerIdx() <4):
                raise Exception("Mentoookkkkk")    
            l[idx] , l[idx-4] = l[idx-4] , l[idx]
        else:
            p.lastDirection = "up"  
            if(self.getPointerIdx() >=12):
                raise Exception("Mentoookkkkk")  
            l[idx] , l[idx+4] = l[idx+4] , l[idx]
        p.matriks = l;
        return p
    
    def getPointerIdx(self):
        return self.matriks.index(16)

    def isBlack(self):
        return (self.getPointerIdx()//4 + self.getPointerIdx()%4) %2 == 1

    def kurangI(self,num):
        kurang = 0
        for i in range (self.matriks.index(num),16):
            if (self.matriks[i] < num):
                    kurang += 1
        return kurang

    def sumKurangI_X(self):
        sum = 0
        for i in range(1,17):
            sum += self.kurangI(i)
        return sum + self.isBlack()

    def canSolve(self):
        return self.sumKurangI_X()%2 ==0
    
    def isSolution(self):
        for i in range(16):
            if (self.matriks[i] != i+1):
                return False
        return True

    def getCost(self):
        g = 0
        for i in range(16):
            if(self.matriks[i]!=i+1):
                g+=1
        return g + self.f

    def __repr__(self):
        s="---------------------\n"
        for i in range(4):
            s+="|"
            for j in range (4):
                s+=" "
                if(self.matriks[i*4+j]<10):
                    s += "0" + str(self.matriks[i*4+j])
                elif(self.matriks[i*4+j]==16):
                    s+= "  "
                else:
                    s+=str(self.matriks[i*4+j])
                s+=" |"
            s+="\n---------------------\n"
        s+= "cost = " + str(self.getCost()) + "\n"
        s+= "Sum Kurang I + X = " + str(self.sumKurangI_X()) + "\n"
        s+= "Mungkin = " + str(self.canSolve()) + "\n"
        s+= "Solusi = " + str(self.isSolution()) + "\n"
        return s
    def __str__(self):
        s="Simpul ke - " + str(self.id)+"\n"
        s+="---------------------\n"
        for i in range(4):
            s+="|"
            for j in range (4):
                s+=" "
                if(self.matriks[i*4+j]<10):
                    s += " " + str(self.matriks[i*4+j])
                elif(self.matriks[i*4+j]==16):
                    s+= "  "
                else:
                    s+=str(self.matriks[i*4+j])
                s+=" |"
            s+="\n---------------------\n"
        return s
    def printBranch(self):
        if(self.before!=None):
            self.before.printBranch()
        print(self)

    def printTabelI(self):
        print("-------------------------")
        print("     i     |    Kurang(i)")
        print("-------------------------")
        for i in range(1, 17):
            print("   ",f'{i:2d}' ,"    |      ",f'{self.kurangI(i):2d}') 
        print("-------------------------")


    def readFile(filename):
        with open(filename,'r') as file:
            l=[int(num)  for line in file for num in line.split(" ")]
        puzzle = Puzzle(l)
        return puzzle
# l=[]
# for i in range(1,17):
#     l.append(i)

# #random.shuffle(l)
# l =[1,2,3,4,5,6,16,8,9,10,7,11,13,14,15,12]
# # l=[1,3,4,15,2,16,5,12,7,6,11,14,8,9,10,13]
# p = Puzzle(l)
# print (repr(p))

# q = p.nextPuzzle("up")
# print (repr(q))

# q.printBranch()

#print (Puzzle.countPuzzle)