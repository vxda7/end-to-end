test_case = int(input())
for case in range(1, test_case + 1):
    D, H, M = map(int, input().split())
    timing = 11*24*60 + 11*60 + 11
    get = D*24*60 + H*60 + M
    if get - timing < 0:
        print("#{} {}".format(case, -1))
    else:
        print("#{} {}".format(case, get - timing))