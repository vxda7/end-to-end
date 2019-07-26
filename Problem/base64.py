# dictonary 만들기
data_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
cnt=0
data_dic={}
for data in data_str:
    data_dic[data]=cnt
    cnt+=1

numbers = int(input())
answer=[]
result=''
for number in range(numbers):       #받은 횟수만큼 돌기
    get = input()                   #한줄 입력받기
    result=''
    temp=''                         #4글자 합칠 곳
    cnt=0
    for i in get:
        become_bin = str(bin(data_dic[i]))[2:]  #0b를 제외한 2진수 문자화
        while len(become_bin) < 6:
            become_bin = '0' + become_bin       #6자리가 아닌 2진수 6자리로

        temp+=become_bin                        #4개의 2진수화된 글자를 합치기
        
        if cnt%4 == 3:
            first_piece = chr(int('0b'+temp[:8],2))
            second_piece = chr(int('0b'+temp[8:16],2))
            third_piece = chr(int('0b'+temp[16:],2))
            result+= first_piece + second_piece + third_piece
            temp=''
        cnt+=1
    answer.append(result)

cnt=1
for i in answer:
    print(f"#{cnt} {i}") 
    cnt+=1