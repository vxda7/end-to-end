def find(gotit,get_number1,get_number2):
    print(gotit)
    a=False
    b=False
    for i in gotit:
        if i == get_number1:
            a=True
        elif i == get_number2:
            b=True

    print(f"{get_number1} => {a}")
    print(f"{get_number2} => {b}")

get_list=[2, 4, 6, 8, 10]
find(get_list,5,10)