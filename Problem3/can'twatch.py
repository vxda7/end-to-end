test_case = int(input())
collection = {'a','e','i','o','u'}
for case in range(test_case):
    gets = input()
    print("#{}".format(case+1),end=" ")
    for get in gets:
        if not get in collection:
            print("{}".format(get),end="")