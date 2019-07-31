numbers = int(input())

def my_timeplus(first_hour, first_minute, last_hour, last_minute):
    result_hour = first_hour + last_hour
    result_minute = first_minute + last_minute

    if result_minute > 59:
        result_minute-=60
        result_hour+=1

    if result_hour > 12:
        result_hour -= 12
    
    result = [result_hour, result_minute]
    return result


result=[]
for number in range(numbers):
    gets = list(map(int,input().split()))

    result.append(my_timeplus(gets[0], gets[1], gets[2], gets[3]))
    
#출력
cnt=1
for res in result:
    print(f"#{cnt} {res[0]} {res[1]}")
    cnt+=1