T = int(input())
for case in range(T):
    H, W = map(int, input().split())
    gamemap = []
    where = True
    for i in range(H):
        gamemap.append(input())
        if '<' in gamemap or where:
            wherey = i
            wherex = gamemap[i].index('<')
            first = False
        elif '>' in gamemap or where:
            wherey = i
            wherex = gamemap[i].index('>')
            first = False
        elif '^' in gamemap or where:
            wherey = i
            wherex = gamemap[i].index('^')
            first = False
        elif 'v' in gamemap or where:
            wherey = i
            wherex = gamemap[i].index('v')
            first = False
            
    # rotgamemap = list(zip(*gamemap))

    N = int(input())
    cmd = input()

    for j in range(N):
        if cmd[j] == 'U' and wherey != H-1:
            if wherey == H-1:
                gamemap[wherey][wherex] = '^'
            else:
                if gamemap[wherey + 1][wherex] == '.':
                    gamemap[wherey][wherex] = '.'
                    gamemap[wherey + 1][wherex] = '^'
        if cmd[j] == 'D' and wherey != 0:
            if wherey == 0:
                gamemap[wherey][wherex] = 'v'
            else:
                if gamemap[wherey - 1][wherex] == '.':
                    gamemap[wherey][wherex] = '.'
                    gamemap[wherey - 1][wherex] = 'v'
        if cmd[j] == 'L':
            if wherex == 0:
                gamemap[wherey][wherex] = '<'
            else:
                if gamemap[wherey][wherex - 1] == '.':
                    gamemap[wherey][wherex] = '.'
                    gamemap[wherey][wherex - 1] = '<'
        if cmd[j] == 'R':
            if wherex == W-1:
                gamemap[wherey][wherex] = '>'
            else:
                if gamemap[wherey][wherex + 1] == '.':
                    gamemap[wherey][wherex] = '.'
                    gamemap[wherey][wherex + 1] = '>'
        
        if cmd[j]  == 'S':
            if gamemap[wherex][wherey] == '^':
                pass
        