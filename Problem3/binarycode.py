def check(gets):
    idx = 0
    for i in range(len(gets)):
        if i % 8 == 0:
            


test_case = int(input())

for case in range(1, test_case + 1):
    height, width = map(int,input().split())
    lines=[]
    for i in range(height):
        lines.append(i)