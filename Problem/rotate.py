numbers = int(input())
results=[]
for number in range(numbers):
    gets = int(input())
    cube=[]
    rot90=[]
    rot180=[]
    rot270=[]
    for get in range(gets):
        rot90.append([])
        rot180.append([])
        rot270.append([])
        cube.append(list(map(int,input().split())))
    for cub in cube:
        cnt=0
        for cu in cub:
            rot90[cnt].insert(0,str(cu))
            rot180[len(cube)-cube.index(cub)-1].insert(0,str(cu))
            rot270[len(cube)-cnt-1].append(str(cu))
            cnt+=1
        ''.join(rot90[cube.index(cub)])

    print(rot90)
    print(rot180)
    print(rot270)
    results.append(rot90)
    results.append(rot180)
    results.append(rot270)

print(results)

# cnt=1
# for result in results:
#     for result
