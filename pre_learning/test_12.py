
get = int(input())
count = [9]
rank = [9]
j = 0

while get>9:
    what=int(get%10)
    rank[j] = what
    if get>9:
        get = int(get/10)
    count[what]=count[what]+1
    j=j+1
    
for i in range(0,10):
    print(i,end=" ")

for i in rank:
    print(i,end=" ")
