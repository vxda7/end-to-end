numbers = int(input())
real=[]
for number in range(numbers):
    get = int(input())
    result=0
    for i in range(1,get+1):
        if i%2:
            result+=i
        else:
            result-=i
    real.append(result)

cnt=1
for i in real:
    print(f'#{cnt} {i}')
    cnt+=1
