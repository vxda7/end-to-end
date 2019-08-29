t = int(input())
for tc in range(1, t+1):
    N = int(input())

    info = []
    best = 0
    for i in range(N):
        row, col, direction, energy = map(int, input().split())
        info.append([row, col, direction, energy])
    #     this = max(abs(row), abs(col))
    #     if best < this:
    #         best = this
    #
    # space = [[0]*best for i in range(best)]
    # table = [[0]*best for i in range(best)]
    #
    # for i in range(N):



    # 경우의 수가 너무 많음
    # 좌상, 상, 우상, 우, 우하, 하, 좌하, 좌
    dr = [-1, 0, 1, 1, 1, 0, -1, -1]
    dc = [-1, -1, -1, 0, 1, 1, 1, 0]

    # 0 1 2 3  x(row), y(col), direction, energy
    for i in range(N):
        for j in range(i, N):
            dir = info[i][2]    # (atomdir+1)*2-1   dr,dc idx
            odir = info[j][2]

            row, col = info[i][0], info[i][1]
            orow, ocol = info[j][0], info[j][1]
            long = max(abs(row-orow), abs(col-ocol))

            # 위
            if dir == 0:
                if odir == 0:   # 같은곳을 향하면 만날 수 없다.
                    break
                else:
                    if odir == 1 and row == orow and col < ocol:    # 위 아래 만남
                        time = ocol - col
                        if len(info[i]) == 4 or len(info[j]) == 4:   # 둘 다 시간 값이 없다면
                            info[i].append(time)
                            info[j].append(time)
                        if len(info[i]) == 5 and len(info[j]) == 4:
                            if info[i][4] > time:   # 기존값이 더 크면
                                info[i][4] = time
                                info[j].append(time)
                        if len(info[i]) == 4 and len(info[j]) == 5:
                            if info[j][4] > time:  # 기존값이 더 크면
                                info[j][4] = time
                                info[j].append(time)
                        else:   # 둘 다 있다면
                            # if info[i][j]
                            pass

                    elif odir == 2 and orow+row == ocol+col and ocol < col:     # 위랑 좌 방향 만남
                        time = ocol - col
                        if len(info[i]) == 4 or len(info[j]) == 4:   # 둘 다 시간 값이 없다면
                            info[i].append(time)
                            info[j].append(time)
                        if len(info[i]) == 5 and len(info[j]) == 4:
                            if info[i][4] > time:   # 기존값이 더 크면
                                info[i][4] = time
                                info[j].append(time)
                        if len(info[i]) == 4 and len(info[j]) == 5:
                            if info[j][4] > time:  # 기존값이 더 크면
                                info[j][4] = time
                                info[j].append(time)
                        else:   # 둘 다 있다면
                            # if info[i][j]
                            pass

                    elif odir == 3 and orow-row == ocol-col and orow > row:     # 위랑 우 방향 만남
                        time = ocol - col
                        if len(info[i]) == 4 or len(info[j]) == 4:   # 둘 다 시간 값이 없다면
                            info[i].append(time)
                            info[j].append(time)
                        if len(info[i]) == 5 and len(info[j]) == 4:
                            if info[i][4] > time:   # 기존값이 더 크면
                                info[i][4] = time
                                info[j].append(time)
                        if len(info[i]) == 4 and len(info[j]) == 5:
                            if info[j][4] > time:  # 기존값이 더 크면
                                info[j][4] = time
                                info[j].append(time)
                        else:   # 둘 다 있다면
                            # if info[i][j]
                            pass


            # if dir == 2 and odir == 3: # 좌우로 만날 조건
            #
            # elif dir == 3 and odir == 2: # 우좌로 만날 조건
