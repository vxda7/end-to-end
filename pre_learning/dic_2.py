have = {
    "TV": 2000000,
    "냉장고": 1500000,
    "책상": 350000,
    "노트북": 1200000,
    "가스레인지": 200000,
    "세탁기": 1000000,
}


def makesort(have,result):
    big=0
    cnt=0
    big_key=''
    for key, value in have.items():
        if big < value:
            big = value
            big_key = key
        else:
            cnt+=1
    if not big_key == '':
        result.append({big_key:big})
    have[big_key]=0
    if cnt==len(have):
        return result
    return makesort(have,result)

result=[]
result_list=makesort(have,result)
print(result_list)
for i in result_list:
    print(f'{list(i.keys())[0]}: {list(i.values())[0]}')