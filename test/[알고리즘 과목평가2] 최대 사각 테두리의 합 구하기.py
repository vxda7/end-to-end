import sys

sys.stdin = open("input2.txt", 'r')

for t in range(int(input())):
    number_row, number_column, number_frame = map(int, input().split())

    list_samples = []
    for _ in range(number_row):
        list_samples.append(list(map(int, input().split())))

    list_frame = []
    for y in range(number_frame):
        for x in [0, number_frame - 1]:
            list_frame.append([x, y])
    for x in range(number_frame):
        for y in [0, number_frame - 1]:
            list_frame.append([x, y])
    list_frame.remove([0, 0])
    list_frame.remove([0, number_frame - 1])
    list_frame.remove([number_frame - 1, 0])
    list_frame.remove([number_frame - 1, number_frame - 1])

    number_ans = 0
    for index in list_frame:
        number_ans += list_samples[index[1]][index[0]]

    for y in range(number_row - number_frame + 1):
        for x in range(number_column - number_frame + 1):
            number_temp = 0
            for index in list_frame:
                number_temp += list_samples[y + index[1]][x + index[0]]
            if number_temp > number_ans:
                number_ans = number_temp
    print(f"#{t+1} {number_ans}")

# 1 40
# 2 40
# 3 614
