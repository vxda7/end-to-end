t = int(input())
for tc in range(1, t+1):
    get = input()
    clap = 0
    employee = 0
    cnt = 0
    while True:
        if cnt == len(get):
            break
        clap += int(get[cnt])
        if clap < cnt+1:
            employee += cnt - clap + 1
        cnt += 1
    print(f"#{tc} {employee}")

    
