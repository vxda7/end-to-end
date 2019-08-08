result = []
for i in range(10):
    numbers = int(input())
    originals = list(map(int,input().split()))
    manys = int(input())
    cmds = list(map(int,input().split()))

    # temp=originals[:]
    for many in range(manys):
        if cmds[many] == 'I':
            x = cmds[many+1]
            y = cmds[many+2]
            s = cmds[many+3: many+3+y]
            originals[x:x+y]=s  #리스트채로 수정

        elif cmds[many] == 'D':
            x = cmds[many+1]
            y = cmds[many+2]
            del originals[x:x+y]

        elif cmds[many] == 'A':
            y = cmds[many+1]
            s = cmds[many+2: many+2+y]

    result.append(originals[0:10])

#출력
cnt=1
for res in result:
    print(f"{cnt}",end=" ")
    for r in res:
        print(f"{r}",end=" ")
    print("")
    cnt+=1



# a = [1,2,3,4,5,6,7,8,9]
# a[0:2] = [0,0]
# print(a)