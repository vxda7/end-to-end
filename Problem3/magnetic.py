def rot90(gets):
    temp=[]
    for i in range(len(gets)):
        temp.append([])
    for get in gets:
        cnt=0
        for g in get:
            temp[cnt].insert(0, g)
            cnt += 1
    return temp

def check(gets):
    gets = rot90(gets)
    change=0
    for get in gets:
        first=False
        save=2
        for g in get:
            if g:
                if first:
                    if g != save:
                        save=g
                        change+=1
                elif g == 2:
                    first=True
    if change%2:
        return int((change+1)/2)
    elif change == 0 :
        return 0
    else:
        return int((change)/2)
                
# 바뀌는 횟수가 짝수면 1빼고 홀수면 1더하기



#test케이스 횟수
result=[]
for num in range(1):
    numbers = int(input())  # 
    # N->1 S->2 up->N down->S
    case=[]
   
    for i in range(numbers):
        gets = list(map(int,input().split()))
        case.append(gets)
    result.append(check(case))

#출력
cnt=1
for res in result:
    print(f"#{cnt} {res}")
    cnt += 1
