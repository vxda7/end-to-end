numbers = int(input())
results=[]

def snail(n):
    num=[]
    for i in range(n):      #빈 2차원배열 생성
        num.append([0]*n)

    edge = n
    term = 0
    cnt=0
    onechain=0

    for i in range(n**2):   #제곱만큼 for문

        if onechain == (edge-1-term)*4:     # 겉에 한바퀴가 돈 것을 체크 (n=5: 16) (n=4: 12) (n=3: 8)순으로 된다
            edge-=1 #한바퀴가 돌면 한칸씩좁아진다.
            term+=1 #간격을 만들어서 한바퀴마다 1씩 바뀌는 요소에 사용
            cnt+=1  # 한줄에 돌때마다 생기는 0 1 2 3 의 순서용
            onechain=0  # 한바퀴가 도는 것을 순서대로 세주는 용도

        if onechain < edge-1-term:      #                                                                               - > ㅇ
            num[n - edge][cnt] = i+1    # n-edge 는 기본적으로 네모의 가장 끝 cnt는  012345, 1234, 23 등으로 세져야한다.   ㅇ ㅇ ㅇ
            if cnt == edge-2:   #이 if절의 마지막일때 cnt를 초기화!                                                      ㅇ ㅇ ㅇ
                cnt=term-1

        elif onechain < (edge-1-term)*2: #                                                          ㅇ ㅇ |
            num[cnt][edge-1] = i+1  #edge는 네모가 줄때 하나씩 줄어들므로 edge-1은 리스트의 가장 끝     ㅇ ㅇ ▽
            if cnt == edge-2:   #                                                                   ㅇ ㅇ ㅇ
                cnt=term-1

        elif onechain < (edge-1-term)*3:
            num[edge - 1][n-1 - cnt] = i+1      # cnt가 term으로 인해 네모가 줄어들때마다 줄어들므로 중복되게 빠지지 않게 n을 써준다.
            if cnt == edge-2:
                cnt=term-1

        elif onechain < (edge-1-term)*4:
            num[n-1 - cnt][n-edge] = i+1
            if cnt == edge-2:
                cnt=term-1
        
        onechain+=1
        cnt+=1

    if n%2:                     # 홀수개는 가장 가운데에 한칸이 생기므로 따로 넣어준다.
        where = n//2
        num[where][where]=n**2

    return num


for number in range(numbers):
    get = int(input())
    results.append(snail(get))

#출력
cnt=1
for result in results:
    print(f"#{cnt}")
    for res in result:
        for r in res:
            print(f"{r}",end=" ")
        print("")
    cnt+=1
