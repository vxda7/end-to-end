test_case = int(input())

for case in range(1,test_case+1):
    get = input()
    print("#{}".format(case),end=" ")
    for i in range(int(get)):
        print("1/{}".format(get),end=" ")
    print("")
