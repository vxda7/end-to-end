result = []
for i in range(10):
    numbers = int(input())
    originals = list(map(int,input().split()))
    manys = int(input())
    cmds = list(input().split())
    # temp=originals[:]

    for many in range(len(cmds)):
        if cmds[many] == 'I':
            x = int(cmds[many+1])
            y = int(cmds[many+2])
            s = cmds[many+3: many+3+y]
            # print(x+1, y, s)
            for i in s[::-1]:
                originals.insert(x,i)

        elif cmds[many] == 'D':
            x = int(cmds[many+1])
            y = int(cmds[many+2])
            del originals[x:x+y+1]

        elif cmds[many] == 'A':
            y = int(cmds[many+1])
            s = cmds[many+2: many+2+y]
            
            for i in s:
                originals.append(s)

    result.append(originals[0:10])

#출력
cnt=1
for res in result:
    print(f"#{cnt}",end=" ")
    for r in res:
        print(f"{r}",end=" ")
    print("")
    cnt+=1

