# import sys
# sys.stdin = open("input.txt","r")

def rot90(table):
    temp=[]
    for i in range(len(table)):
        temp.append([])
    for row in table:
        cnt=0
        for a in row:
            temp[cnt].insert(0,a)
            cnt+=1
    return temp

def which(a,b):
    if a>b:
        return a
    else:
        return b

def find(table):
    best=1
    n=0
    before=0
    for row in table:   # 한줄씩 빼오는 for
        for j in range(100):   #한줄을 여러번 돌기위한 for
            for i in range(100-n+1):   # 한줄을 도는 for
                piece = row[i:i+n]
                if piece == piece[::-1]:
                    best=n
                    break
            n+=1
        n=best
    return best


for test_case in range(1,11):
    case = int(input())
    table=[]
    for i in range(100):
        table.append(input())
    result = which(find(table), find(rot90(table)))
    print("#{0} {1}".format(test_case, result))