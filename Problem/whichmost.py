numbers = int(input())

result=[]
for number in range(numbers):
    get = list(map(int,input().split(' ')))
    result.append(max(get))
cnt=1
for i in result:
    print(f"#{cnt} {i}")
    cnt+=1