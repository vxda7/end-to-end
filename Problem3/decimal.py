n = 1000000
num =[False]*2 + [True] * (n-1)
m = 1000
for i in range(2, m+1):
    if num[i] == True:
        for j in range(i+i, n+1, i):
            num[j] = False

for k in range(n+1):
    if num[k] == True:
        print(k,end=" ")
