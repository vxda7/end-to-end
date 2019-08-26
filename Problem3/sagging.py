result = []
t = int(input())
for tc in range(1, t+1):
    get = list(input())
    hipen = int(input())
    idx = list(map(int, input().split()))
    cnt = 0
    idx.sort()
    for i in idx:
        get.insert(i+cnt,'-')
        cnt +=1
    result.append(''.join(get))

for i in range(t):
    print(f"#{i+1} {result[i]}")