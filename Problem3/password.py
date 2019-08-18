# import sys
# sys.stdin = open("input (6).txt","r")

for test_case in range(1,11):
    length, numbers = input().split()
    length = int(length)
    numbers = list(numbers)
    idx = 0
    for go in range(length + int(length//2)):   # 아무리 쌍이 여러개가 나와도 길이의 1.5배 이상 돌 필요가 없다
        num_length = len(numbers) 
        if idx == num_length-1:
            break
        else:
            if numbers[idx] == numbers[idx + 1]:
                del numbers[idx: idx + 2]   #2개를 지우고 싶다면 2
                idx -= 2    #1이 추가될 것을 고려해서 -2
        idx += 1
    
    print("#{} {}".format(test_case, ''.join(numbers)))