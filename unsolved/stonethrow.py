numbers = int(input())
result=[]
cnt_result=[]

for number in range(numbers):
    people = int(input())
    records = list(map(int,input().split()))
    best = min(list(map(abs,records)))
    cnt=0
    # 비교
    for record in records:
        if abs(record) == best:
            cnt+=1

    result.append(best)
    cnt_result.append(cnt)

# 출력
cnt=1
for res in result:
    print(f"#{cnt} {res} {cnt_result[result.index(res)]}")
    cnt+=1
        
        
