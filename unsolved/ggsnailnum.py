numbers = int(input())
result=[]
def snail(n):
    num=[]
    for i in range(n):      #빈 2차원배열 생성
        num.append([]*n)

    right_edge = n-1
    down_edge = n-1
    left_edge = 0
    up_edge = 0
    cnt=0
    for i in range(1,n**2+1):
        if cnt < right_edge:
            num[up_edge].insert(right_edge,i)
        elif n <= cnt:
            num[i//n].insert(right_edge,i)
        elif True:
            num[down_edge].insert(0,i)
        elif True:
            num[n-1-i//n].insert(0,i)

        right_edge -= 1
        down_edge -= 1
        left_edge += 1
        up_edge += 1
        cnt+=1
    return num

for number in range(numbers):
    get = int(input())
    print(snail(get))

