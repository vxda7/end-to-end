centence = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
del_list = ['a','e','i','o','u']
result = ''
for i in centence:
    if i in del_list:
        result+=""
    else:
        result+=i
        
print(result)

