def cheap(get):
    pass

numbers = int(input())

result=[]
for number in range(numbers):
    get = list(map(int,input().split()))
    get_p = get[0]
    get_q = get[1]
    get_r = get[2]
    get_s = get[3]
    get_w = get[4]
    if get_w - get_r > 0:
        overfee = get_w - get_r
    else:
        overfee = 0
    if get_p * get_w > get_q + overfee * get_s:
        result.append(get_q + overfee * get_s)
    else:
        result.append(get_p * get_w)

cnt = 1
for i in result:
    print(f'#{cnt} {i}')
    cnt+=1