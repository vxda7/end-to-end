first=True

for i in range(100,301):
    hundred=i//100
    tens=(i-hundred*100)//10
    ones=i-hundred*100-tens*10
    
    if hundred%2==0 and tens%2==0 and ones%2==0 and first==False:
        print(",%d" %i,end="")
    elif hundred%2==0 and tens%2==0 and ones%2==0 and first==True:
        print("%d" %i,end="")
        first=False
