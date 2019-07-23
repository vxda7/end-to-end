import math
PI = math.pi

get = input().split(', ')
result = []
for i in get:
    result.append(int(i))
first = True
for i in result:
    if not first:
        print(",",end=" ")
    first = False
    print(f"{i*2*PI:0.2f}",end="")