t = int(input())
for tc in range(1, t+1):
    get = input()
    even = {'0', '2', '4', '6', '8'}
    if get[-1] in even:
        print(f"#{tc} Even")
    else:
        print(f"#{tc} Odd")