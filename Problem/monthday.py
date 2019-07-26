calender = {'1':31, '2':28, '3':31, '4':30, '5':31, '6':30, '7':31, '8':31, '9':30, '10':31, '11':30, '12':31}

numbers = int(input())
result = []

def check(fm,fd,lm,ld,sumall):
    if fm == lm:
        sumall += (ld - fd)+1
        return sumall
    else:
        for i in range(lm-fm):
            sumall += (calender[str(fm)]-fd+1)
            fm += 1
            fd = 1
        sumall+= ld-fd+1
        return sumall
    
for number in range(numbers):
    get = list(map(int,input().split()))
    first_m = get[0]
    first_d = get[1]
    last_m = get[2]
    last_d = get[3]
    sumall=0
    result.append(check(first_m, first_d, last_m, last_d, sumall))

cnt=1
for res in result:
    print(f'#{cnt} {res}')
    cnt+=1


        
        
