get = input()

cnt_upper=0
cnt_lower=0
for i in get:
    if i.isupper():
        cnt_upper+=1
    elif i.islower():
        cnt_lower+=1

print(f"UPPER CASE {cnt_upper}")
print(f"LOWER CASE {cnt_lower}")
