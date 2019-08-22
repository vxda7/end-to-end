cha = [True] * 1000001
cha[0:1] = [False, False]
for i in range(2, 1000001):
    if cha[i]:
        for j in range(i+i, 1000001, i):
            cha[j] = False

test_case = int(input())
for case in range(1, test_case + 1):
    D, A, B = map(int, input().split())
    cnt = 0
    for i in range(A,B+1):
        if cha[i]:
            if str(D) in str(i):
                cnt+=1
    print("#{} {}".format(case, cnt))