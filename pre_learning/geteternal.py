get = input()
while get!="":
    try:
        result = get.upper()
        print(f'>> {result}')
        get = input()
    except:
        break
