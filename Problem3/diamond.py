t = int(input())
for tc in range(1, t+1):
    get = input()
    length = len(get)
    for j in range(length):
        if j == 0:
            print("..#..",end="")
        else:
            print(".#..",end="")
        if j == length - 1:
            print()

    for j in range(length):
        if j == 0:
            print(".#.#.",end="")
        else:
            print("#.#.",end="")
        if j == length - 1:
            print()

    for j in range(length):
        if j == 0:
            print(f"#.{get[j]}.#",end="")
        else:
            print(".{}.#".format(get[j]),end="")
        if j == length - 1:
            print()

    for j in range(length):
        if j == 0:
            print(".#.#.",end="")
        else:
            print("#.#.",end="")
        if j == length - 1:
            print()

    for j in range(length):
        if j == 0:
            print("..#..",end="")
        else:
            print(".#..",end="")
        if j == length - 1:
            print()
    

            