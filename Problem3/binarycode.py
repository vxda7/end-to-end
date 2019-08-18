test_case = int(input())

for case in range(1, test_case + 1):
    height, width = map(int,input().split())
    lines=[]
    for i in range(height):
        lines.append(i)