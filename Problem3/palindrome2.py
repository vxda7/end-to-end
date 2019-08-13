def rot90(table):
    temp=[[]]*100
    for row in table:
        cnt=0
        for a in row:
            temp[cnt].insert(0,a)
            cnt+=1
    return temp

def find(table):
    best=0
    for row in table:
        n=2
        for i in range(100-n):
            piece = row[i:i+n]
            if piece == piece[::-1]:
                best=n
                n+=1
                break
                
def which(a,b):
    if a>b:
        return a
    else:
        return b

for test_case in range(10):
    case = int(input())
    table=[]
    for i in range(100):
        table.append(input())
    result = which(find(table), find(rot90(table)))
    print("#{0} {1}".format(test_case,result))
