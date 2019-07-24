get = list(map(int,input().split(' ')))

if get[0] == 1 and get [1] == 3:
    print('A')
elif get[0] == 3 and get[1] == 1:
    print('B')
elif get[0] > get[1]:
    print('A')
else:
    print('B')