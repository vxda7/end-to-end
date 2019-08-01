numbers = int(input())

result=''

def check(number):
    number = number.replace('3','-')
    number = number.replace('6','-')
    number = number.replace('9','-')

    if number.count('-') > 0:
        return '-'*number.count('-')
    else:
        return str(number)
    

for number in range(1,numbers+1):
    result+=check(str(number))+' '

print(result)

    