import sys
sys.stdin = open("input (13).txt", "r")

test_case = int(input())

for case in range(1, test_case + 1):
    height, width = map(int,input().split())
    lines=[]
    for i in range(height):
        lines.append(input())
    for line in lines:
        if line.index('1'):
            idx = line.index('1')
            