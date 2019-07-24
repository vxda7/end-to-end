numbers = int(input())
result=[]
for number in range(numbers):
    get = list(map(int,input().split(' ')))
    result.append(sum(get)/len(get))
cnt=1
for i in result:
    print(f"#{cnt} {int(round(i,0))}")
    cnt+=1