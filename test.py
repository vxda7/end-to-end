
score=[85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
sum=0
pp=0
i=0
lo=len(score)

while i<lo:
    i=i+1
    pp=score.pop()
    if pp>=80:
        sum+=pp
        
print(sum)