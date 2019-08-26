result = []
t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    score = list(map(int, input().split()))
    result.append(sum(sorted(score)[-k:]))
for i in range(t):
    print("#{} {}".format(i+1, result[i]))
