for t in range(1, int(input())+1):
    n = int(input())
    card = input().split()
    print("#{}".format(t), end=" ")
    num = len(card)//2
    if n%2:
        part_one = card[:num+2]
        part_two = card[num+1:]
    else:
        part_one = card[:num+1]
        part_two = card[num:]
    
    if n%2:
        for i in range(num):
            print("{}".format(part_one[i]), end=" ")
            print("{}".format(part_two[i]), end=" ")
        print("{}".format(part_one[i+1]), end=" ")
    else:
        for i in range(num):
            print("{}".format(part_one[i]), end=" ")
            print("{}".format(part_two[i]), end=" ")
    print()