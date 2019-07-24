get = int(input())
result=[]

for i in range(get):
    numlong = int(input())
    numbers = list(map(int,input()))
    best = max(numbers)
    differ=[]
    
    for number in range(len(numbers)):
        if number != numbers[-1]:
            differ.append(numbers[number+1]-numbers[number])
