
result = []
this = [result.append(1) if i==0 or i == 1 else result.append(result[i-2]+result[i-1]) for i in range(10)]

print(result)