numbers = int(input())

result=[]
for number in range(numbers):
    others = int(input())
    velocity=0
    where=0
    for other in range(others):
        gets = list(map(int,input().split()))
    
        if gets[0] == 0:
            plus=0
        elif gets[0] == 1:
            plus=gets[1]
        else:
            plus=-gets[1]
        
        if velocity + plus >= 0:
            velocity+=plus
        else:
            velocity=0
        where+=velocity
    result.append(where)

#출력
cnt=1
for res in result:
    print(f"#{cnt} {res}")
    cnt+=1