get = input().split(', ')

get_list = [i for i in get if int(i)%2]
first = True
for i in get_list:
    if first:
        print(i,end='')
        first = False
    else:
        print(f', {i}',end="")