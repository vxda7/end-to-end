t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    nums = {key:value for key,value in enumerate([False]*n,1)}
    get = list(map(int, input().split()))
    for i in get:
        nums[i] = True
    
    print(f"#{tc}",end=' ')
    for key in nums:
        if not nums[key]:
            print(f"{key}",end=' ')
    print()