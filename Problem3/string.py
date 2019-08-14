for i in range(10):
    test_case = int(input())
    want = input()
    gets = input()
    count=0
    for get in range(len(gets)-len(want)+1):
        if gets[get:get+len(want)] == want:
            count+=1

    print("#{} {}".format(test_case,count))