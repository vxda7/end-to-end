test_case = int(input())
for case in range(1, test_case + 1):
    N = int(input())
    A = list(input().split())
    best = -1
    for i in range(N - 1):
        ok = True
        part = ''.join(A[i:i+2])
        for j in range(len(part)-1):
            if int(part[j]) > int(part[j + 1]):
                ok = False
        if ok:        
            mul = int(A[i]) * int(A[i + 1])
            if best < mul:
                best = mul
    print("#{} {}".format(case, best))