
def isitok(days):
    box = [31,28,31,30,31,30,31,31,30,31,30,31]
    if not(1 <= int(days[4:6]) <= 12):
        return -1
    elif 1 <= int(days[6:]) <= box[int(days[4:6])-1]:
        return days[0:4]+'/'+days[4:6]+'/'+days[6:]
    else:
        return -1

numbers = int(input())
result = []
for number in range(numbers):
    get = input()
    result.append(isitok(get))

cnt=1
for i in result:
    print(f"#{cnt} {i}")
    cnt+=1
