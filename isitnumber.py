get = input()
cnt_letter=0
cnt_number=0
for i in get:
    if i.isdigit():
        cnt_number+=1
    elif i.isalpha():
        cnt_letter+=1

print(f'LETTERS {cnt_letter}')
print(f'DIGITS {cnt_number}')
