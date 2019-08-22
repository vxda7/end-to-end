t = int(input())
for case in range(1, t + 1):
    a, b, c = input().split()
    if a == b:
        print("#{} {}".format(case, c))
    elif b == c:
        print("#{} {}".format(case, a))
    else:
        print("#{} {}".format(case, b))
        