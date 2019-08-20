# import sys
# sys.stdin = open("input (15).txt", "r")

T = int(input())
for case in range(1, T+1):
    H, W = map(int, input().split())
    gamemap = []
    where = True
    for i in range(H):
        get = list(input())
        gamemap.append(get)
        if '<' in get and where:
            wherey = i
            wherex = get.index('<')
            first = False
        elif '>' in get and where:
            wherey = i
            wherex = get.index('>')
            first = False
        elif '^' in get and where:
            wherey = i
            wherex = get.index('^')
            first = False
        elif 'v' in get and where:
            wherey = i
            wherex = get.index('v')
            first = False

    N = int(input())
    cmd = input()
    
    for j in range(N):
        # for i in range(H):
        #     print(''.join(gamemap[i]))
        # print(wherey, wherex)
        if cmd[j] == 'U':
            if wherey == 0:
                gamemap[wherey][wherex] = '^'
            elif gamemap[wherey - 1][wherex] == '-' or gamemap[wherey - 1][wherex] == '#' or gamemap[wherey - 1][wherex] == '*':
                gamemap[wherey][wherex] = '^'
            else:
                if gamemap[wherey - 1][wherex] == '.':
                    gamemap[wherey][wherex] = '.'
                    gamemap[wherey - 1][wherex] = '^'
                    wherey -= 1
        if cmd[j] == 'D':
            if wherey == H-1:
                gamemap[wherey][wherex] = 'v'
            elif gamemap[wherey + 1][wherex] == '-' or gamemap[wherey + 1][wherex] == '#' or gamemap[wherey + 1][wherex] == '*':
                gamemap[wherey][wherex] = 'v'
            else:
                if gamemap[wherey + 1][wherex] == '.':
                    gamemap[wherey][wherex] = '.'
                    gamemap[wherey + 1][wherex] = 'v'
                    wherey += 1
        if cmd[j] == 'L':
            if wherex == 0:
                gamemap[wherey][wherex] = '<'
            elif gamemap[wherey][wherex - 1] == '-' or gamemap[wherey][wherex - 1] == '#' or gamemap[wherey][wherex - 1] == '*':
                gamemap[wherey][wherex] = '<'
            else:
                if gamemap[wherey][wherex - 1] == '.':
                    gamemap[wherey][wherex] = '.'
                    gamemap[wherey][wherex - 1] = '<'
                    wherex -= 1
        if cmd[j] == 'R':
            if wherex == W-1:
                gamemap[wherey][wherex] = '>'
            elif gamemap[wherey][wherex + 1] == '-' or gamemap[wherey][wherex + 1] == '#' or gamemap[wherey][wherex + 1] == '*':
                gamemap[wherey][wherex] = '>'
            else:
                if gamemap[wherey][wherex + 1] == '.':
                    gamemap[wherey][wherex] = '.'
                    gamemap[wherey][wherex + 1] = '>'
                    wherex += 1
        
        if cmd[j]  == 'S':
            if gamemap[wherey][wherex] == '^':
                for k in range(wherey, -1, -1):
                    if gamemap[k][wherex] == '*':
                        gamemap[k][wherex] = '.'
                        break
                    elif gamemap[k][wherex] == '#':
                        break
            if gamemap[wherey][wherex] == 'v':
                for k in range(wherey+1, H):
                    if gamemap[k][wherex] == '*':
                        gamemap[k][wherex] = '.'
                        break
                    elif gamemap[k][wherex] == '#':
                        break
            if gamemap[wherey][wherex] == '>':
                for k in range(wherex + 1, W):
                    if gamemap[wherey][k] == '*':
                        gamemap[wherey][k] = '.'
                        break
                    elif gamemap[wherey][k] == '#':
                        break
            if gamemap[wherey][wherex] == '<':
                for k in range(wherex, -1, -1):
                    if gamemap[wherey][k] == '*':
                        gamemap[wherey][k] = '.'
                        break
                    elif gamemap[wherey][k] == '#':
                        break
            
    print("#{}".format(case),end=" ")
    for i in range(H):
        print(''.join(gamemap[i]))

        