
# def in_cache(func):
#     cache = {}
#     def wrapper(n):
#         if n in cache:
#             return cache[n]
#         else:
#             cache[n] = func(n)
#             return cache[n]
#     return wrapper


# @in_cache
# def factorial(N):
#     result = 1
#     for i in range(1,N+1):
#         result *= i
#     return result

import math

test_case = int(input())

for case in range(1,test_case+1):
    N, R = map(int, input().split())
    result = math.factorial(N) // math.factorial(N-R) // math.factorial(R)  % 1234567891

    print("#{} {}".format(case, result))
