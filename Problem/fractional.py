numbers = int(input())

result=[]
for number in range(numbers):
    get = int(input())
    result.append({'2':0, '3':0, '5':0, '7':0, '11':0})
    cnt=0
    temp=-1
    while True:
        if cnt == temp:
            break
        temp = cnt

        if get%2 == 0:
            result[number]['2']+=1
            cnt+=1
            get=get/2

        elif get%3 == 0:
            result[number]['3']+=1
            cnt+=1
            get=get/3
        elif get%5 == 0:
            result[number]['5']+=1
            cnt+=1
            get=get/5

        elif get%7 == 0:
            result[number]['7']+=1
            cnt+=1
            get=get/7

        elif get%11 == 0:
            result[number]['11']+=1
            cnt+=1
            get=get/11

cnt=1
for i in result:
    print(f'#{cnt}',end=' ')
    for key,value in i.items():    
        print(f'{value}',end=' ')
    cnt+=1

    