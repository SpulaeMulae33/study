import random
N = int(input('Input matrix size N: '))
M = int(input('Now M: '))

A = [ [0]* M for i in range(M)]

for i in range(N):
    for j in range(M):
        A[i][j] = random.randint(10,99)

for i in range(len(A)):
    for j in range(len(A[i])):
        if len(A[i]) == 2:
            print(A[i][j], end = ' ')
        else:
            print(A[i][j], end = '   ')
    print()

string = len(A)
row = len(A[i])

#for i in range(len(A)):
#    for j in range(len(A[i])):
