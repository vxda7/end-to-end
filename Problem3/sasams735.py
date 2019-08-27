t = int(input())
for tc in range(1, t+1):
    get = list(map(int, input().split()))
    
    allpart = []
    for i in range(1<<7):
        temp=[]
        for j in range(len(get)):
            if i&(1<<j):
                temp.append(get[j])
        if len(temp) == 3:
            allpart.append(temp)
    best = 0
    for i in allpart:
        res = sum(i)
        if best < res:
            best = res
    print("#{} {}".format(tc, best))

