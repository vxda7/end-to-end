numbers = int(input())
result=[]


def lineok(gets):
    if sum(gets) == 45:
        if len(list(set(gets))) == 9:
            return 1
        else:
            return 0
    else:
        return 0


for number in range(numbers):
    rot90=[]
    cubes=[]
    rights=[]
    answer=1

    for nines in range(1,10):
        rot90.append([])
        cubes.append([])
        gets = list(map(int,input().split()))
        rights.append(gets)
    
    linecnt=0
    for right in rights:
        cnt=0
        for r in right:
            rot90[8-cnt].insert(0,r)
            cubes[cnt//3 + (linecnt//3)*3].append(r)
            cnt+=1
        linecnt+=1

    for nines in range(9):
        answer = lineok(rights[nines])
        if answer == 0:
            break
        answer = lineok(rot90[nines])
        if answer == 0:
            break
        answer = lineok(cubes[nines])
        if answer == 0:
            break
    # print(rot90)
    # print(cubes)
    result.append(answer)

cnt=1
for res in result:
    print(f"#{cnt} {res}")
    cnt+=1