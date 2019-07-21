get = [12, 24, 35, 70, 88, 120, 155]

result = [get[i] for i in range(len(get)) if not(i==0 or i==4 or i==5)]
print(result)