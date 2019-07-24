number = int(input())
result=[]
for i in range(number):
    get = map(int,input().split(' '))
    result.append(sum(g for g in get if g%2))

cnt=1
for i in result:
    print(f'#{cnt} {i}')
    cnt+=1