numbers = int(input())
result = []

def empty(n):
    temp=[]
    for i in range(n):
        temp.append([0]*n)

def laydown(temp, x, y):
    temp[x][:]+=1
    temp[:][y]+=1
    #대각선
    for i in len(temp):
        for j in len(temp):
            if x+y == i+j:
                temp[i][j]+=1
            elif x-y == i-j:
                temp[i][j]+=1
    temp[x][y]+=100
    return temp

def check(n):
    howmany=0
    temp=0
    cube = empty(n)

    for i in range(n):
        for j in range(n):
            cube = laydown(cube, i, j)
            




    return howmany

for number in range(numbers):
    gets = int(input())

