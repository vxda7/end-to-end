test_case=int(input())

for case in range(1, test_case+1):
    numbers = int(input())
    result=0
    for number in range(numbers):
        p,money = map(float,input().split())
        result += p*money
    print("#{0} {1}".format(case,result))