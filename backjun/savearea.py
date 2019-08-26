def find(num, n):
    global area
    stack = []
    result = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    this = [area[i][:] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if this[i][j] > num:
                print(this)
                result += 1
                stack.append([i,j])
                while len(stack) != 0:
                    pi, pj = stack.pop()
                    this[pi][pj] = 0
                    for k in range(4):
                        ni = pi + di[k]
                        nj = pj + dj[k]
                        if 0 <= ni < n and 0 <= nj < n:
                            if this[ni][nj] > num:
                                stack.append([ni,nj])
    return result


n = int(input())
area = []
best = 0
for i in range(n):
    get = list(map(int, input().split()))
    area.append(get)
    temp = max(get)
    if temp > best:
        best = temp
        
most = 0
for j in range(1, best):
    temp = find(j, n)
    if most < temp:
        most = temp
print(most)