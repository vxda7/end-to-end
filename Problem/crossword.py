numbers = int(input())

def findword(get, temp):
    for i in temp:
        for j in i:
            if j == 1:
                if j





for number in range(numbers):
    get = list(map(int,input().split()))
    temp=[]
    for i in range(get[0]):
        get_cross = list(map(int,input().split()))
        temp.append(get_cross)
    findword(get[1], temp)