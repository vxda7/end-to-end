t = int(input())
for tc in range(1, t+1):
    get = input()
    clap = 0
    employee = 0
    cnt = 0
    while True:
        if cnt == len(get):
            break
        if clap < cnt:
            employee += cnt - clap
            clap += cnt - clap
        clap += int(get[cnt])
        cnt += 1
    print(f"#{tc} {employee}")

    
