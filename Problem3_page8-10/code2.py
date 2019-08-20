# import sys
# sys.stdin = open("input (5).txt", "r")

for test_case in range(1,11):
    code_length = int(input())
    original = list(map(int, input().split()))
    cmd_length = int(input())
    cmd = input().split()

    for one in range(len(cmd)):
        if cmd[one] == 'I':
            x = int(cmd[one + 1])
            y = int(cmd[one + 2])
            s = cmd[one + 3 : one + 3 + y]
            for i in s[::-1]:
                original.insert(x, int(i))

        if cmd[one] == 'D':
            x = int(cmd[one + 1])
            y = int(cmd[one + 2])
            del original[x: x + y]

    print("#{}".format(test_case),end=" ")
    for j in range(10):
        print("{}".format(original[j]),end=" ")
    print()

