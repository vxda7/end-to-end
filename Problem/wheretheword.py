numbers = int(input())
result=[]
for number in range(numbers):
    gets = list(map(int,input().split()))
    result_cnt=0
    lines=[]
    rot90=[]
    for get in range(gets[0]):
        rot90.append([])
        lines.append(list(map(int,input().split())))
    
    for line in lines:
        rcnt=0
        for one in line:
            rot90[len(lines) - 1 - rcnt].insert(0,one)
            rcnt+=1            


    for line in lines:
        cnt=0
        for one in line:
            cnt+=one
            if one == 0:
                cnt=0
            elif cnt == gets[1]:
                result_cnt += 1
                # print(one, result_cnt)
            elif cnt > gets[1]:
                result_cnt -= 1
                cnt=-100


    # print(lines)
    # print(rot90)
    # print(result_cnt)

    for rot in rot90:
        cnt=0
        for one in rot:
            cnt+=one
            if one == 0:
                cnt=0
            elif cnt == gets[1]:
                result_cnt += 1
                # print(one, result_cnt)
            elif cnt > gets[1]:
                result_cnt -= 1
                cnt=-100


    result.append(result_cnt)

cnt=1
for res in result:
    print(f"#{cnt} {res}")
    cnt+=1
