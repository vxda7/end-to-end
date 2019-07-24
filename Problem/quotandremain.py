numbers = int(input())
result=[]
for number in range(numbers):
    get = list(map(int,input().split(' ')))
    result.append((get[0]//get[1],get[0]%get[1]))
cnt=1
for i in result:
    print(f"#{cnt} {i[0]} {i[1]}")
    cnt+=1