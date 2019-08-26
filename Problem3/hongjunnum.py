result = []
T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    which = min(a, b)

    resx = 0
    resy = 0
    for x in range(1, which+1):
        y = (1 - a*x)//b
        if a*x + b*y == 1:
            resx = x
            resy = y
            result.append([resx, int(resy)])
            break
    else:
        result.append([-1, ' '])

for i in range(T):
    print("#{} {} {}".format(i+1, *result[i]))