get = '3, 5' #input()
get_list = get.split(", ")

result = []
temp = []
for i in range(int(get_list[0])):
    temp = []
    for j in range(int(get_list[1])):
        temp.append(i*j)
    result.append(temp)

print(result)