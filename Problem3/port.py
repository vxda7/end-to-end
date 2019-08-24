t = int(input())
for case in range(1, t+1):
    n = int(input())
    gets = []
    num = []
    for i in range(n):
        gets.append(int(input()))
    num.append(gets[1]-1)
    for i in gets[2:]:
        for j in num:
            if (i-1)%j == 0:
                break
            else:
                num.append(i-1)
    # print(num)
    result = len(num)   
    print("#{} {}".format(case, result))



# 값은 나오지만 시간이 너무 오래걸림
# t = int(input())
# for case in range(1, t+1):
#     n = int(input())
#     gets = []
#     for i in range(n):
#         gets.append(int(input()))

#     space = [0]*(gets[-1]+1)

#     for i in range(n):
#         space[gets[i]] = 1 

#     for i in gets[1:]:
#         for j in range(i+i-1,gets[-1] + 1,i-1):
#             print(j)
#             space[j] = 0 
#     result = sum(space)
#     print("#{} {}".format(case, result-1))