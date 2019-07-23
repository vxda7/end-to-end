temp_number=0

for i in range(1,201):
    if(i%7==0 and not i%5==0 and not temp_number==0):
        print(",%d" %i, end='')
    elif(i%7==0 and not i%5==0 and temp_number==0):
        print("%d" %i, end='')
        temp_number+=1
