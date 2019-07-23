def my_sqrt(get):
    list_sample = [i**2 for i in range(1,get+1)]
    print(list_sample)
    for i in range(len(list_sample)):
        if get < list_sample[i]:
            first_try = i
            second_try = i+1
            print(first_try)
            print(second_try)
            break
    print(get)

    close = (first_try + second_try) / 2
    for i in range(11):
        print(close)
        if  close**2 < get:
            first_try = close
            close = (close + second_try) / 2
            
        else:
            second_try =close
            close = (close + first_try) / 2
    return(close)

get = int(input())
my_sqrt(get)




