# numbers = int(input())
# result=[]

# def rich(values):
#     best=max(values)
    
#     for value in values:
#         if value < best:
#             temp.append(best-value)
#         elif values.index(value) == len(values)-1:
#             pass
#         elif value == best:
#             best=max(values[values.index(value)+1:])

# for number in range(numbers):
#     temp=[0]
#     gets = int(input())
#     values = list(map(int,input().split()))
#     rich(values)
#     # print(temp)
#     result.append(sum(temp))

# #출력
# cnt=1
# for res in result:
#     print(f"#{cnt} {res}")
#     cnt+=1

numbers = int(input())
result=[]

for number in range(numbers):
    gets = int(input())
    values = list(map(int,input().split()))
    mini = -1
    res=0    
    for value in reversed(values):
        if value > mini:
            mini = value
        else:
            res += mini - value
    
    result.append(res)

cnt=1
for res in result:
    print("#{} {}".format(cnt, res))
    cnt+=1