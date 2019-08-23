result = []
t = int(input())
for case in range(1, t + 1):
    a, b, c, d = map(int, input().split())
    alice = a/b
    bob = c/d
    if alice > bob:
        result.append("ALICE")
    elif alice < bob:
        result.append("BOB")
    else:
        result.append("DRAW")

for i in range(t):
    print("#{} {}".format(i+1, result[i]))
