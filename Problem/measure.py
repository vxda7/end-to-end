get = int(input())
result=[]
for i in range(1,get+1):
        if get%i == 0:
            result.append(i)

for i in result:
    print(f"{i}",end=" ")