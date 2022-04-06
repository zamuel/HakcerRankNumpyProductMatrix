#Multiplicar matrices cuadradas
#hacker rank en numpy
import numpy as np

n = int(input())

arrA = np.ones((n,n),dtype=int)
arrB = np.ones((n,n),dtype=int)
arrC = np.ones((n,n),dtype=int)

for i in range(n):
    row = input().strip().split(' ')
    row1 = [int(r) for r in row]
    arrA[i] = row1

for i in range(n):
    row = input().strip().split(' ')
    row1 = [int(r) for r in row]
    arrB[i] = row1

for i in range(n):
    for j in range(n):
        arrC[i,j]=np.dot(arrA[i],arrB[:,j])
print(arrC)
