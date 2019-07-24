get = input()

result=""
for i in get:
    if ord('a') <= ord(i) <= ord('z'):
        result += str(ord(i)-ord('a'))+" "
    elif ord('A') <= ord(i) <= ord('Z'):
        result += str(ord(i)-ord('A')+1)+" "

print(result)