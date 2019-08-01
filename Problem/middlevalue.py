numbers = int(input())
result=[]

for number in range(numbers):
    thisnumber = input()
    score_list=list(map(int,input().split()))
    get_score=[0]*101

    for score in score_list:
        get_score[score]+=1
    #print(get_score)
    get_score = list(reversed(get_score))
    value = get_score.index(max(get_score))
    result.append(100-value)

#출력
cnt=1
for res in result:
    print(f"#{cnt} {res}")
    cnt+=1
