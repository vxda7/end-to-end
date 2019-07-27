numbers = int(input())

result=[]
for number in range(numbers):
    gets = int(input())

    for get in range(gets):
        temp=[]
        if get == 0:
            temp.append(1)
        elif get == 1:
            temp.append(1)
            temp.append(1)
        else:
            for i in range(get+1):
                if i == 0:
                    temp.append(1)
                elif i == get:
                    temp.append(1)
                else:
                    temp.append(result[get-1][i-1]+result[get-1][i])
        result.append(temp)

print(result)
cnt=1
for res in result:
    print(f'#{cnt}',end=' ')
    line=''
    for char in res:
        line+=str(char)+' '
    print(f'{line}')
    cnt+=1