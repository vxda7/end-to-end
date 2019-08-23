# Space, Diamond, Heart, Clover
t = int(input())
for case in range(1, t+1):
    info = input()
    data = []
    sdhc = [13, 13, 13, 13]
    error = False
    for j in range(0, len(info),3):
        if info[j] == 'S':
            sdhc[0] -= 1
        elif info[j] == 'D':
            sdhc[1] -= 1
        elif info[j] == 'H':
            sdhc[2] -= 1
        elif info[j] == 'C':
            sdhc[3] -= 1

        if info[j: j+3] not in data:
            data.append(info[j: j+3])
        else:
            error = True
    if error:
        print("#{} ERROR".format(case))
    else:
        print("#{} {} {} {} {}".format(case, sdhc[0], sdhc[1], sdhc[2], sdhc[3]))