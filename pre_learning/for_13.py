get=input()

get_list=list(get)
howlong=len(get_list)
what_list=[]
text=""
for i in range(howlong):
    text=get_list[howlong-1-i]
    what_list.append(text)
    

if get_list==what_list:
    print(get)
    print("입력하신 단어는 회문(Palindrome)입니다.")
else:
    print(get)
    print("입력하신 단어는 회문(Palindrome)이 아닙니다.")