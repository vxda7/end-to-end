def what(*arg):
    result=1
    for i in arg:
        if type(i) == int:
            result*=i
        else:
            return '에러발생'
    return result

print(what(1, 2, '4', 3))