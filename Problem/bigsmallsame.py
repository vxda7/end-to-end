numbers = int(input())
result=[]
for number in range(numbers):
    get = list(map(int,input().split(' ')))
    if get[0] > get[1]:
        result.append('>')
    elif get[0] < get[1]:
        result.append('<')
    else:
        result.append('=')
    
cnt=1
for i in result:
    print(f'#{cnt} {i}')
    cnt+=1