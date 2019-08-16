import math
import sys

sys.stdin = open("input (11).txt", "r")

# A * abs(R - C) + B * (N - R*C)
def find(N, A, B):
    result = 0
    close = int(math.sqrt(N))
    half_close = int(close//2)
    temp=[]
    if A >= B+5:
        R,C = close, close
        result = A * abs(R - C) + B * (N - R*C)
    elif A < B:
        for j in range(N,close,-1):
            for i in range(half_close, j):
                if N % i == 0:
                    R = i
                    C = int(N//i)
                    temp.append(A * abs(R - C) + B * (N - R*C))
        if temp:
            result = min(temp)
    return result


def isdecimal(number):
    for i in range(2,int(math.sqrt(number)+1)):
        if number % i == 0:
            result = False
            return result
    return True


# def find(N, A, B):
#     # B-A만큼 돌아도 정사각형의 결과보다 
#     # A 와 N - int(math.sqrt(N))**2
#     for i in range(N):
#         pass

test_case = int(input())
for case in range(1, test_case + 1):
    N, A, B = map(int,input().split())
    result = find(N,A,B)
    print("#{} {}".format(case, result))