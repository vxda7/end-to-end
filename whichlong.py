def which(get):
    get_list=get.replace(" ","").split(",")
    if len(get_list[0]) > len(get_list[1]):
        print(get_list[0])
    elif len(get_list[0]) < len(get_list[1]):
        print(get_list[1])
    else:
        print("둘의 길이가 같습니다.")

geta=input()

which(geta)