t = int(input())
for tc in range(1, t+1):
    six = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    #   1월 1일 금요일:4
    m, d = map(int, input().split())
    allday = 0
    if m != 1:
        for i in range(1,m):
            allday += six[i]
    allday += d
    res = (allday + 3) % 7
    print(f"#{tc} {res}")
    
    