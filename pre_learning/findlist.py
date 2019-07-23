get_first = [1,3,6,78,35,55]
get_second = [12,24,35,24,88,120,155]

def givemetwolist(get_first,get_second):
    for i in get_first:
        if i in get_second:
            return [i]

print(givemetwolist(get_first,get_second))