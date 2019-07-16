get = {'a' : 0, 'b' : 1, 'c' : 2, 'd' :3, 'e' : 4, 'f' :5}
print(get)
get_key = list(get.keys())
print(get_key)
get_value = list(get.values())
print(get_value)

for i in range(len(get_key)):
    print(f"{get_key[i]}: {get_value[i]}")
