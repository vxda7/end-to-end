result = []
t = int(input())
for tc in range(1, t+1):
    get = input()
    palindrome = True
    for i in range(len(get)//2):
        if get[i] == get[-i-1] or get[i] == '?' or get[-i-1] == '?':
            pass
        else:
            palindrome = False
    
    if palindrome:
        result.append("Exist")
    else: 
        result.append("Not exist")

for i in range(t):
    print(f"#{i+1} {result[i]}")