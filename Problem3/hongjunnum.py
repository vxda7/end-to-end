import sys
sys.stdin = open("sample_input (2).txt",'r')

# result = []
# T = int(input())
# for tc in range(1, T+1):
#     a, b = map(int, input().split())
#     which = min(a, b)

#     resx = 0
#     resy = 0
#     for x in range(1, which+1):
#         y = (1 - a*x)//b
#         if a*x + b*y == 1:
#             resx = x
#             resy = y
#             result.append([resx, int(resy)])
#             break
#     else:
#         result.append([-1, ' '])

# for i in range(T):
#     print("#{} {} {}".format(i+1, *result[i]))

def which(a, b):
        if a > b:
            return a, b
        else:
            return b, a


def find(big, small):
    r1, r2 = big, small
    s1, s2 = 1, 0
    t1, t2 = 0, 1
    while r2 != 0: 
        q = big//small
        r = r1 - q * r2
        r1, r2 = r2, r
        
        s = s1 - q * s2
        s1, s2 = s2, s

        t = t1 - q * t2
        t1, t2 = t2, t

    return a,b

    

            
result = []
T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    big, small = which(a,b)
    result.append(find(big, small))

for i in range(T):
    print("#{} {} {}".format(i+1, *result[i]))