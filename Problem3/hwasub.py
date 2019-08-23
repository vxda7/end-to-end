# import sys
# sys.stdin = open("sample_input (11).txt", "r")

t = int(input())
for i in range(1, t + 1):
    n = int(input())
    nums = []
    while True:
        nums += input().split()
        if len(nums) == n:
            break
    nums = ''.join(nums)

    compare = 0
    small = 0
    while True:
        if str(compare) not in nums:
            small = compare
            break
        compare += 1 
    
    print("#{} {}".format(i, small))
