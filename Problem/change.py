numbers=int(input())
result=[]

for number in range(numbers):
    temp=[]
    gets = int(input())

    pays=[50000, 10000, 5000, 1000, 500, 100, 50, 10]

    for pay in pays:
        temp.append(gets // pay)
        gets-=pay*(gets//pay)
    
    result.append(temp)

#출력
cnt=1
for res in result:
    print(f"#{cnt}")
    for r in res:
        print(f"{r}",end=" ")
    cnt+=1
    print("")