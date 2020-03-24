# import random
# import copy
# l=[]
# for i in range(1,17):
#     l.append(i)
# k = l.copy()
# random.shuffle(k)

# print(l)
# print(k)
# l =[1,2,3,4,5,6,16,8,9,10,7,11,13,14,15,12]
# # random.shuffle(l)
# # print(l)
# kurang = 0
# for i in range(1,17):
#     for j in range (l.index(i),16):
#         if (l[j] < i):
#             kurang += 1
#     print(i,end=" ")
#     print(kurang)

        
    


# #print(kurang + l.index(16)+1)
with open('input.txt', 'r') as f:
    l=[int(num)  for line in f for num in line.split(" ")]

print(l)