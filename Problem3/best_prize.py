def check(val, cnt):
    val = list(str(val))
    print(val)
    samecnt=0
    smallcnt=0
    for i in range(cnt):
        sortval = sorted(val)
        sortedval = list(reversed(sortval))
        print(sortedval)
        
        if i != 0:
            if sortedval[i] == sortedval[i - 1]:
                samecnt += 1
            else:
                samecnt = 1

        if i != 0:
            if sortval[i] == sortval[i - 1]:
                smallcnt += 1
            else:
                smallcnt = 1

        vai = sortedval.index(sortedval[i], smallcnt)
        svai = len(val) -1 - sortedval.index(sortedval[i], samecnt)
        print(vai)
        print(svai)
        if vai != svai:
            val[vai], val[svai] = val[svai], val[vai]
        print(val)
    return val


test_case = int(input())

for case in range(1, test_case + 1):
    value, cnt = map(int, input().split())
    result = check(value, cnt)
    print("#{} {}".format(test_case, result))