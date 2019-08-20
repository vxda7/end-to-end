# import sys
# sys.stdin = open("input (14).txt", 'r')

test_case = int(input())
for case in range(1, test_case+1):
    N, M, P = map(int, input().split())
    gets = list(map(int, input().split()))
    gets.sort()
    save = 0
    cnt = 0
    for i in range(0,11112):
        if i % M == 0 and i != 0:
            save += P
        if i == gets[cnt]:
            save -= gets.count(gets[cnt])
            cnt += 1
        if save < 0:
            result = "Impossible"
            break
        if i == gets[-1]:
            result = "Possible"
            break

    print("#{} {}".format(case, result))