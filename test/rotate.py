numbers = int(input())


lcnt=1
for number in range(numbers):
    gets = int(input())
    result=[]
    answers=[]

    rot90=[]
    rot180=[]
    rot270=[]

    cubes = []
    for get in range(gets):
        rot90.append([])
        rot180.append([])
        rot270.append([])
        answers.append([])
        cubes.append(list(map(int,input().split())))

    for cube in cubes:
        cnt=0   # 몇번째 라인에 있는지 세줌
        for cu in cube:
            rot90[cnt].insert(0,cu)
            rot180[len(cube) - 1 - cubes.index(cube)].insert(0,cu)
            rot270[len(cube)-cnt-1].append(cu)
            cnt += 1
    
    result.append(rot90)
    result.append(rot180)
    result.append(rot270)


    for res in result:
        cnt=0
        for i in range(len(res)):
            answers[i].append(res[i])

    #출력
    print(f"#{lcnt}")
    for answer in answers:
        for ans in answer:
            for a in ans:
                print(f"{a}",end="")
            print("",end=" ")
        print("")
    lcnt+=1

