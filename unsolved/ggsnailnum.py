numbers = int(input())
result=[]
def snail(n):
    num=[]
    for i in range(n):      #빈 2차원배열 생성
        num.append([]*n)

    border = n-1
    turn = 0
    for i in range(n):   #규칙을 찾자
        num.append(i+1)

    cnt=0
    for i in range((n-1)*2):

        num[cnt-1-x].insert(0,i+1)

        num[n-1+x].insert(0,i+1)

        num[0+x].insert(0,i+1)

        num[cnt-2-x]


        cnt += 1
        
                



        # if i <= n*1-0:
        #     num[0][i]=i+1


        # elif i <= n*2-1:
        #     num[i-n][n-1]=i+1
        # elif i <= n*3-2:
        #     num[n-1][(n*3-2)-i)]=i+1
        # elif i <= n*4-4:
        #     num[(n*4-4)-i][0]=i+1
        # elif i <= n*5-6:
        #     num[1][i-(n*4-4)]=i+1

        # elif i <= n*6-7

        

for number in range(numbers):
    get = int(input())
