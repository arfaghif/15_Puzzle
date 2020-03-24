import time
import argparse
from PrioQueue import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help ="Menerima inputan nama file yang akan dibaca")
    args = parser.parse_args()
    
    try:
        startPuzzle= Puzzle.readFile("../TestCase/"+args.filename)
        print("Matriks posisi awal sebagai berikut :")
        print(startPuzzle)
        print("Berikut tabel kurang(i) matriks awal ")
        startPuzzle.printTabelI()
        print("Berikut nilai Sigma Kurang(i) + X Matriks Awal : ", startPuzzle.sumKurangI_X())
        print()
        print("Berikut rute yang diambil :")
        startTime = time.time_ns()
        myPrioQueue= PrioQueue(startPuzzle)
        finishPuzzle = myPrioQueue.run()
        finishTime = time.time_ns()
        finishPuzzle.printBranch()   
    except Exception as error:
        finishTime = time.time_ns()
        print("Error: " + str(error))
    except KeyboardInterrupt:
        finishTime = time.time_ns()
        print("Error: Puzzle terlalu rumit") 
    finally:
        print("Waktu eksekusi : " , finishTime-startTime, "nanosekon")
        print("Jumlah simpul yang dibangkitkan : " ,Puzzle.countPuzzle)