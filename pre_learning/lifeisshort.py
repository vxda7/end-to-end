my_str = "Life is too short, you need python"
howlong = len(my_str)

for i in range(howlong):
    #print(my_str[i])
    if my_str[i] == 'a' or my_str[i] == 'e' or my_str[i] == 'i' or  my_str[i] == 'o' or my_str[i] == 'u':
        print("",end="")
    else:
        print(my_str[i],end="")