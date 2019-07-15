def whichone(get):
    geta=get.split(", ")[0]
    getb=get.split(", ")[1]
    
    if len(geta)>len(getb):
        print(geta)
    else:
        print(getb)


get=input()
whichone(get)