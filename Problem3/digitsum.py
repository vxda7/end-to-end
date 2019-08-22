t = int(input())
result = []
for case in range(1, t + 1):
    n = input()
    while len(n) != 1:
        temp = 0
        for i in range(len(n)):
            temp += int(n[i])
        n = str(temp)
    result.append(n)

for i in range(t):
    print("#{} {}".format(i+1, result[i]))