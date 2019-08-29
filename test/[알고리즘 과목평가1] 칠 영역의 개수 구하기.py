import sys

sys.stdin = open("input1.txt", 'r')

for t in range(int(input())):
    number_size_table, number_commands = map(int, input().split())
    list_list_table = [[0 for _ in range(number_size_table)] for _ in range(number_size_table)]
    for _ in range(number_commands):
        y1, x1, y2, x2 = map(lambda x: int(x) - 1, input().split())
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                list_list_table[y][x] = 1
    cnt = 0
    for y in range(number_size_table):
        for x in range(number_size_table):
            if list_list_table[y][x] == 1:
                cnt += 1
    print(f"#{t+1} {cnt}")

# 1 12
# 2 29
# 3 243
