numbers = int(input())

results=[]
for number in range(numbers):
    temp=''
    howmanys = int(input())
    for howmany in range(howmanys):
        gets = input().split()
        temp += gets[0]*int(gets[1])
    results.append(temp)

print(results)
#출력
cnt=1
for result in results:
    print(f"#{cnt}")
    cnt+=1
    enter=0
    for res in result:
        print(f"{res}",end="")
        enter+=1
        if enter % 10 ==0:
            print("")
    print("")
        