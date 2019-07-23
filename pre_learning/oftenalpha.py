get = input()
result=[0]*26
for i in get:
    i.lower()
    result[ord(i)-ord('a')]+=1

print(result)
cnt=0    
for i in result:
    if i != 0:
        a = chr(ord('a')+cnt)
        print(f"{a},{i}")
    cnt+=1
