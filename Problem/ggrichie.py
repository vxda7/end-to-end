get = int(input())
result=[]

for i in range(get):
    numlong = int(input())
    numbers = list(map(int,input().split()))
    tempsum=0

    best = max(numbers)
    # where = numbers.index(best)
    for i in range(numlong):
        if numbers[i] < best:
            tempsum+=best-numbers[i]
        else:
            if numbers[numbers.index(best)] == numbers[-1]:
                pass
            else:
                best = max(numbers[numbers.index(best)+1:])
    result.append(tempsum)

cnt=1
for i in result:
    print(f'#{cnt} {i}')
    cnt+=1

#1트 max를 for 문안에 넣으면 용량은 192메가지만 30초를 초과함
#2트 max를 밖으로 빼고 index를 활용하면 1초면 되지만 265메가로 용량초과
#3트 where 을 없애고 넣어주면 3메가 줄고 시간은 1.5초 현재 262메가







# get = int(input())
# result=[]

# for i in range(get):
#     numlong = int(input())
#     numbers = list(map(int,input().split()))
#     tempsum=0
#     updown=[]
#     start=0
#     for j in range(numlong):
#         if numbers[j] == numbers[-1]:
#             pass
#         else:
#             diff = numbers[j+1] - numbers[j]
#             if diff < 0:
#                 end=j #numbers.index(numbers[j])
#                 if start == j:
#                     pass
#                 else:
#                     best = max(numbers[start:end])
#                     for k in numbers[start:end]:
#                         tempsum+=numbers[end]-k
#                     start=end+1
#             else:
#                 end=j
#                 if start == j:
#                     pass
#                 else:
#                     best = max(numbers[start:end])
#                     for k in numbers[start:end]:
#                         tempsum+=numbers[end]-k
#                     start=end+1


#     result.append(tempsum)

# cnt=1
# for i in result:
#     print(f'#{cnt} {i}')
#     cnt+=1