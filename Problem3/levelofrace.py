# python이 없었음
def level(number, blocks):
    for i in range(number):
        if i == number:
            break
        else:
            blocks[i]-blocks[i+1]


    max_value
    min_value


test_case = int(input())

for case in range(1,test_case+1):
    number = int(input())
    blocks = list(map(int,input().split()))
    result = level(number, blocks)
    print("#{0} {1} {2}".format(case, result[0], result[1]))
