my_str = "Life is too short, you need python"
howlong = len(my_str)

collection=['a', 'e', 'i', 'o', 'u']
result=[]

for i in my_str:
    if i not in collection:
        result.append(i)

print(''.join(result))