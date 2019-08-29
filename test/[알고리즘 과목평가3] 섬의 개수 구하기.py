import sys

sys.stdin = open("input3.txt", 'r')

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

for t in range(int(input())):
    number_size_earth = int(input())
    list_list_geography = [list(map(int, input().split())) for _ in range(number_size_earth)]
    number_cnt = 0
    for y in range(number_size_earth):
        for x in range(number_size_earth):
            if list_list_geography[y][x]:
                list_list_geography[y][x] = 0
                stack = [[x, y]]
                while len(stack) != 0:
                    temp_stack = []
                    while len(stack) != 0:
                        list_start_point = stack.pop()
                        for _ in range(8):
                            new_x = list_start_point[0] + dx[_]
                            new_y = list_start_point[1] + dy[_]
                            if 0 <= new_x < number_size_earth and 0 <= new_y < number_size_earth:
                                if list_list_geography[new_y][new_x]:
                                    list_list_geography[new_y][new_x] = 0
                                    temp_stack.append([new_x, new_y])
                    for temp in temp_stack:
                        stack.append(temp)
                number_cnt += 1
    print(f"#{t+1} {number_cnt}")

# 1 2
# 2 3
