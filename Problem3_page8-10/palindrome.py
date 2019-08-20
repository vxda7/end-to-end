# 회문인지 확인하고 True or False
def isitpalindrome(word):
    if word[::-1] == word:
        return True
    else:
        return False

# 90도 회전!
def rot90(words):
    result=[[], [], [], [], [], [], [], []]
    for word in words:
        cnt=0
        for char in word:
            result[cnt].insert(0,char)
            cnt+=1
    print(result)
    return result

#글자가 몇개 있는지 확인
def check(words, n):
    rot_words = rot90(words)
    cnt=0
    for word in words:
        for i in range(9-n):
            if isitpalindrome(word[i:n+i]):
                cnt+=1
    for rot_word in rot_words:
        for i in range(9-n):
            if isitpalindrome(rot_word[i:n+i]):
                cnt+=1
    return cnt

result=[]
for tens in range(1):
    number = int(input())
    case=[]
    for i in range(8):
        case.append(input())
    result.append(check(case, number))

#출력
cnt=1
for res in result:
    print(f"#{cnt} {res}")
    cnt += 1