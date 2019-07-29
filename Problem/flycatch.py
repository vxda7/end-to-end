numbers = int(input())
result=[]
for number in range(numbers):
    get = list(map(int,input().split()))
    where = []
    for i in range(get[0]):
        where.append(list(map(int,input().split())))
    
    best=0
    for i in range(get[0]-(get[1]-1)):
        for j in range(get[0]-(get[1]-1)):
            this=0
            for k in range(get[1]):
                this += sum(where[i+k][j:j+get[1]])
            if this > best:
                best=this
    result.append(best)

#출력
cnt = 1
for res in result:
    print(f'#{cnt} {res}')
    cnt+=1
