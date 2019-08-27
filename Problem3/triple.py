t = int(input())
for tc in range(1, t+1):
    n = int(input())
    res = round(n**(1/3))
    if res**3 == n:
        print(f"#{tc} {res}")
    else:
        print(f"#{tc} -1")
         