def my_plus(x,y):
    return x+y

def my_minus(x,y):
    return x-y

def my_multiply(x,y):
    return x*y

def my_division(x,y):
    try:
        x/y
    except:
        return '0으로는 나눌 수 없습니다.'
    else:
        return x/y