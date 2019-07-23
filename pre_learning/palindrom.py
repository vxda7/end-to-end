get = input()
isitpalin=True
howlong = int(len(get)/2)
for i in range(howlong):
    if get[i] == get[-(i+1)]:
        isitpalin=True
    else:
        isitpalin=False
        print("입력하신 단어는 회문이 아닙니다.")
if isitpalin:
    print(get)
    print("입력하신 단어는 회문(Palindrome)입니다.")