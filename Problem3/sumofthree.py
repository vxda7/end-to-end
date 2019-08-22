t = int(input())
for case in range(1, t+1):
    n = int(input())
    s1 = n*(n+1)//2
    s3 = s1*2
    s2 = s3 - n
    print("#{} {} {} {}".format(case, s1, s2, s3))