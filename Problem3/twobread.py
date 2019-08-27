res = []
t = int(input())
for tc in range(1, t+1):
    a, b, c = map(int, input().split())
    small = 0
    if a > b:
        small = b
    else:
        small = a
    
    res.append(c // small)

for i in range(t):
    print(f"#{i+1} {res[i]}")
