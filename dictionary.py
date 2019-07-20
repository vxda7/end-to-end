get = input()
result = []
get = get.split(', ')
result = sorted(get)
for i in result:
    print(f'{i}',end="")
    if i != result[len(result)-1]:
        print(', ',end="")

    