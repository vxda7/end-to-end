a = {'아메리카노': 1900, '카페모카': 3300, '에스프레소': 1900, '카페라떼': 2500, '카푸치노': 2500, '바닐라라떼': 2900}
b = {'헤이즐럿라떼': 2900, '카페모카': 3300, '밀크커피': 3300, '아메리카노': 1900, '샷크린티라떼': 3300}

for i in a:
    b[i] = a[i]

temp =[]
for i in b:
    if b[i] < 3000:
        temp.append(i)

result=[]
for i in temp:
    del(b[i])
for key,value in b.items():
    b=(key,value)
    result.append(b)

print(set(result))
