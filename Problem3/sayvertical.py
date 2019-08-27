t = int(input())
for tc in range(1, t+1):
    table = []
    bestlen = 0
    for i in range(5):
        get = input()
        table.append(get)
        if len(get) > bestlen:
            bestlen = len(get)

    every = []
    for j in range(bestlen):
        for i in range(5):
            if j < len(table[i]):
                every.append(table[i][j])
    
    print(f"#{tc} {''.join(every)}")
        
