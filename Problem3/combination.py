def in_cache(func):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = func(n)
            return cache[n]
    return wrapper


@in_cache
def factorial(N):
    result = 1
    for i in range(1,N+1):
        result *= i
    return result



test_case = int(input())
#콤비네이션을 쓰자! nCm
for case in range(1,test_case+1):
    N, R = map(int, input().split())

    result = factorial(N) / factorial(N-R) /factorial(R)

    print("#{} {}".format(case, int(result % 1234567891)))
