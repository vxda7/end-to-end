get_str=input()
get_len=len(get_str)
count = [0]*10
j = 0
for i in range(get_len):
    count[int(get_str[i])]+=1
    
for i in range(10):
    print(i,end=" ")
print("")
for i in range(10):
    print(count[i],end=" ")
print("")
