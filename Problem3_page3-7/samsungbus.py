test_case = int(input())
for case in range(1, test_case + 1):
    N = int(input())
    A=[]
    B=[]
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    P = int(input())
    C=[]
    for i in range(P):
        C.append(int(input()))
    print("#{}".format(case),end=" ")

    for j in range(P):
        cnt=0
        for i in range(N):
            if A[i] <= C[j] <= B[i]:
                cnt += 1
        print("{}".format(cnt),end=" ")
    print()