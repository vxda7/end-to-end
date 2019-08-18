import sys
sys.stdin = open("GNS_test_input.txt", "r")

alien = {
    "ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9
    }

earth = {
    0:"ZRO", 1:"ONE", 2:"TWO", 3:"THR", 4:"FOR", 5:"FIV", 6:"SIX", 7:"SVN", 8:"EGT", 9:"NIN"
    }

test_case = int(input())
for case in range(test_case):
    gets = input().split()
    numbers = []
    aline_list = input().split()
    for i in aline_list:
        numbers.append(alien[i])
    
    numbers.sort()

    #출력
    print("{}".format(gets[0]))
    
    for number in numbers:
        number = earth[number]
        print("{}".format(number),end=" ")
    print()