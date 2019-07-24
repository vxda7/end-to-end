numbers = int(input())

get = list(map(int,input().split(' ')))
print(sorted(get)[int(numbers/2-0.5)])