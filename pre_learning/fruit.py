fruit = ['   apple    ','banana','  melon']

result={}
for i in fruit:
    i=i.strip(' ')
    result[i]=len(i)

print(result)