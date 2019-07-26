def palind(get):
    if get == get[::-1]:
        return 1
    else:
        return 0

numbers = int(input())
result=[]
for number in range(numbers):
    get = input()
    result.append(palind(get))

cnt=1
for res in result:
    print(f'#{cnt} {res}')
    cnt+=1