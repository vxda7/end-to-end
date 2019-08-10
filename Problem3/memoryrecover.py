numbers = int(input())

def check(gets):
    count=0
    for i in range(len(gets)+1):
        if len(gets) == 0:
            return count
        elif gets[-1] == '0':
            count+=1
            gets = gets.rstrip('0')
        elif gets[-1] == '1':
            count+=1
            gets = gets.rstrip('1')

for number in range(numbers):
    gets = input().lstrip('0')
    result=0
    if len(set(gets)) == 1:
        result=1
    else:
        result=check(gets)

    print("#{0} {1}".format(number+1, result))
