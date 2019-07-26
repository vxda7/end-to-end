numbers = int(input())

def sheep(get):
    empty={}
    empty=set(empty)
    for i in range(get,get*100,get):
        for j in str(i):
            if j not in empty:
                empty.add(j)
                
        if empty == {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
            return i

result=[]

for number in range(numbers):
    get=int(input())
    
    result.append(sheep(get))

cnt=1
for res in result:
    print(f"#{cnt} {res}")
    cnt+=1