numbers = int(input())          # #다음에 적을 숫자


result=[]
for number in range(numbers):      #input을 순서대로 하기위한 깃발숫자
    howlong = list(map(int,input().split()))    #i 와 j의 길이 리스트 받기
    get_i = list(map(int,input().split()))      #i 받기
    get_j = list(map(int,input().split()))      #j 받기

    if howlong[0] > howlong[1]:
        get_i, get_j = get_j, get_i
        howlong.sort()

    diff = howlong[1] - howlong[0] + 1          #i와 j의 길이의 차이 + 1
    temp=[]     #i와 j의 움직이지 않을 때 곱의 합 저장소

    for di in range(diff):      #diff만큼 둘의 위치를 바꾸며 비교
        sumall=0
        for check in range(howlong[0]):
            sumall += get_i[check] * get_j[check+di]
        temp.append(sumall)
    result.append(max(temp))

cnt=1
for res in result:
    print(f'#{cnt} {res}')
    cnt+=1

