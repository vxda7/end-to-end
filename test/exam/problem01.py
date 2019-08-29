def find(n, get):
    res = -1
    sortget = sorted(get)
    rsortget = reversed(sortget)
    temp = []  # 정렬되었는지 확인
    for i in range(5):
        left = get[:n//2]
        right = get[n//2:]
        for j in range(6):  # x 값
            temp = [0] * n
            for k in range(6):
                if j < n//2:
                    if left != []:
                        temp[k] = left.pop(0)
                    else:
                        temp[k] = right.pop(0)
                else:
                    if right != []:
                        temp[k] = right.pop(0)
                    else:
                        temp[k] = left.pop(0)

    return res


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    get = list(map(int, input().split()))
    cnt = find(n, get)
    print("#{} {}".format(tc, cnt))


0
123456  lll rrr 000111  7
1
124356  llr lrr 001011  11
2
142536  lrlrlr  010101  21
3
415263  rlrlrl  101010  42
4
451623  rrlrll  110100  52
5
456123  rrrlll  111000  56