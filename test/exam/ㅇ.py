import sys
import time
start = time.time()
sys.stdin = open("sample_input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    N = int(input())

    info = []
    best = 0
    for i in range(N):
        row, col, direction, energy = map(int, input().split())
        info.append([row, col, direction, energy])

    dx = [0, 0, -0.5, 0.5]
    dy = [0.5, -0.5, 0, 0]

    time = 0
    energy = 0
    while True:
        if time >= 2002 or info == []:
            break

        for i in range(N):
            dir = info[i][2]
            info[i][0] += dx[dir]
            info[i][1] += dy[dir]

        stack = set()
        for i in range(N):
            for j in range(i+1, N):
                if info[i][0] == info[j][0] and info[i][1] == info[j][1]:
                    stack.add(i)
                    stack.add(j)

        stack = list(stack)
        stack.sort()
        while stack:
            it = stack.pop()
            energy += info[it][3]
            del info[it]
            N -= 1

        time += 0.5

    print("#{} {}".format(tc, energy))

print("time : {}".format(start - time.time()))