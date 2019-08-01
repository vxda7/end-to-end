numbers = int(input())
result=[]

for number in range(numbers):
    gets = list(map(int,input().split()))
    gets.remove(max(gets))
    gets.remove(min(gets))
    answer = round(sum(gets) / len(gets))
    result.append(answer)

cnt=1
for res in result:
    print(f"#{cnt} {res}")
    cnt+=1


