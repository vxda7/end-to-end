def decoding(n):
    temp = 0
    cnt = 0
    for i in range(1, n+1):
        temp += i
        if n <= temp:
            temp -= i
            cnt = i - 1
            break

    x = n - temp
    y = cnt + 1 - x + 1
    return x, y


def encoding(x, y):
    n = 0
    for i in range(1,x+y):
        n += i
    result = n - y + 1
    return result


test_case = int(input())

for case in range(1, test_case+1):
    p, q = map(int, input().split())
    x1, y1 = decoding(p)
    x2, y2 = decoding(q)
    result = encoding(x1+x2, y1+y2)
    print("#{} {}".format(case, result))