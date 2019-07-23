get = input().split(' ')
result=[]
for i in range(1,len(get)+1):
    result.append(get[-i])

for i in result:
    print(i,end=' ')