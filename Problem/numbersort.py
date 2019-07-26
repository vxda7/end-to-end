numbers = int(input())

result = []

for number in range(numbers):
    howlong = int(input())
    get = list(map(int,input().split()))

    result.append(sorted(get))

cnt = 1
for res in result:
    print(f'#{cnt}',end=' ')
    for i in res:
        print(f'{i}',end=' ')
    print('')
    cnt+=1