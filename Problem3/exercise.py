numbers = int(input())

result=[]
for number in range(numbers):
    gets = list(map(int,input().split()))

    if gets[2] > gets[1]:
        result.append(-1)
    elif gets[2] < gets[0]:
        result.append(gets[0]-gets[2])
    else:
        result.append(0)

#출력
cnt=1
for res in result:
    print(f"#{cnt} {res}")
    cnt+=1