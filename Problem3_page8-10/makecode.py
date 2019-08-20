def decode(gets):
    while True:
        for i in range(1,6):
            if gets[0]-i <= 0:
                gets.pop(0)
                gets.append(0)
                return gets
            else:
                gets.append(gets.pop(0)-i)

for i in range(10):
    test_case = int(input())
    gets = list(map(int,input().split()))
    gets = decode(gets)
    print("#{}".format(test_case),end=" ")
    for get in gets:
        print("{}".format(get),end=" ")
    print("")