text = input()
howlong=len(text)

if(howlong%2==1):
    solution=int(howlong/2-0.5)    # 5개의 글자 중 가운데는 3번째이지만 리스트내부에서는
    print(text[solution])          #2가 되기때문에 2를나누고 0.5를 빼면 원하는 값이나옴
    
elif(howlong%2==0):
    solve=int(howlong/2)
    print(text[solve-1:solve+1])