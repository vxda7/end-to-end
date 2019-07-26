numbers = int(input())


result=[]
for number in range(numbers):
    get = input()
    temp=''
    one=0
    cnt=0
    for g in get:
        if one>=2:
            if temp[0] == g:
                if temp == get[one:one+len(temp)]:
                    this=get[one:one+len(temp)]
                    cnt+=1
        if cnt==1:
            howlong = len(temp)
            break
        temp+=g    
        one+=1

    result.append(howlong)

num=1
for res in result:
    print(f"#{num} {res}")
    num+=1