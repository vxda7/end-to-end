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
    change=0    # 몇번 바뀌는지 확인하는 것을 세서 교착상태를 확인
    for get in gets:
        first=False #처음에 나오는 수가 2가 아니면 의미가 없음 테이블 밑으로 떨어지므로
        save=2  # 왼쪽이 S극 = 2 이고 오른쪽이 N극 = 1
        temp=0  # 하나의 라인마다 저장할 데이터
        for g in get:
            if g:   # 값이 0이면 건너뜀
                if first:   # 첫값이 2인지 확인 
                    if g != save:   # 저장되어있는 값과 다르면 temp를 1올려줌
                        save=g  # 받은 값을 저장
                        temp+=1 # 임시 change를 1추가
                elif g == 2:    #첫값이 2이면 first를 True로 바꿔서 시작
                    first=True
             
        if temp%2:  # 홀수일 때는 변화량보다 1더한 값의 절반만큼 교착상태
            change += int((temp+1)/2)
        elif temp == 0 :
            change += 0
        else:   # 짝수일 때는 변화량의 절반만큼 교착상태
            change += int((temp)/2)

    return change   # 교착상태의 수를 반환
                
# 바뀌는 횟수가 짝수면 1빼고 홀수면 1더하기

#test케이스 횟수
result=[]
for num in range(10):
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
    print("#{0} {1}".format(cnt, res))
    cnt += 1
