def check(x, list_number_stack):
    y = len(list_number_stack)
    for j, i in enumerate(list_number_stack):
        if x == i or y == j or abs(x - i) == abs(y - j):
            return False
    return True


def n_queen(n):
    list_number_stack = []
    bool_is_back_tracking = False
    number_last_x = -1
    number_cnt = 0
    while len(list_number_stack) != 0 or number_last_x != n - 1:
        for x in range(0 + (number_last_x + 1) * bool_is_back_tracking, n):
            if check(x, list_number_stack):
                list_number_stack.append(x)
                if len(list_number_stack) == n:
                    number_cnt += 1
                    bool_is_back_tracking = True
                    number_last_x = list_number_stack.pop()
                else:
                    number_last_x = x
                    bool_is_back_tracking = False
                break
        else:
            number_last_x = list_number_stack.pop()
            bool_is_back_tracking = True
    print(f"{n}-queen has {number_cnt} solutions!!")


for size in range(1, 16):
    n_queen(size)
