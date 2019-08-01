numbers = int(input())
score_list=['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
result=[]

for number in range(numbers):
    gets = list(map(int,input().split()))
    score=0
    temp=[]
    want=gets[1]
    for get in range(gets[0]):
        score_get = list(map(int,input().split()))
        temp.append(round(score_get[0]*0.35 + score_get[1]*0.45 + score_get[2]*0.2,2))
        if want-1 == get:
            want = temp[-1]
    print(temp)
    temp=list(reversed(sorted(temp)))
    print(temp)
    unit = len(temp) // 10
    result.append(score_list[int(temp.index(want)/unit)])

#출력
cnt=1
for res in result:
    print(f"#{cnt} {res}")
    cnt+=1