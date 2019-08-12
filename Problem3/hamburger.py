# # 콤비네이션은 너무나도 메모리를 많이 차지 한당
# from itertools import combinations
# def makecase(point, cal):
#     point_list=[]
#     cal_list=[]
#     choose = len(point)
#     for i in range(1,choose+1):
#         point_list.extend(combinations(point, i))
#         cal_list.extend(combinations(cal, i))
#
#     for i in cal_list:
#         cal_list[cal_list.index(i)] = sum(list(i))
#
#     for i in point_list:
#         point_list[point_list.index(i)] = sum(list(i))
#
#     where=0
#     best=0
#     for i in range(len(cal_list)):
#         if cal_list[i] <= 1000:
#             if best < point_list[i]:
#                 best = point_list[i]
#                 where = i
#     print(point_list)
#     print(cal_list)
#     print(where)
#     print(best)
#     return point_list[where]


# 콤비네이션 다이어트
def hap(calory,cal, point):
    temp = [point[cal.index(ca)] for ca in calory]
    return sum(temp)

from itertools import combinations
def makecase(point, cal):
    cal_list=[]
    choose = len(point)
    for i in range(1,choose+1):
        cal_list.extend(combinations(cal, i))

    result = [i for i in cal_list if sum(i) <= 1000]
    best = [hap(r,cal,point) for r in result]
    return max(best)

# # 콤비네이션이 아닌 방법을 쓰자
# def makecase(point, cal):
#     point_list=[]
#     cal_list=[]
#     choose = 1
#     best=0
#     while True:
#         if sum(cal[0:choose]) <=1000:
#             if best > sum(point[0:choose]):
#
#     return point


numbers = int(input())

for number in range(numbers):
    gets = list(map(int, input().split()))
    point=[]
    cal=[]
    all=[]
    for get in range(gets[0]):
        cases = list(map(int, input().split()))
        all.extend(cases)
        point.append(cases[0])
        cal.append(cases[1])
    print("#{0} {1}".format(number+1, makecase(point, cal)))
