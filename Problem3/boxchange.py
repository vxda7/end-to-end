t = int(input())
for tc in range(1, t+1):
    n, q = map(int, input().split())
    boxs = [0]*n
    for i in range(q):
        l, r = map(int, input().split())
        boxs[l-1:r] = [i+1]*(r-l+1)
    print(f"#{tc}", end=" ")
    print(*boxs)
