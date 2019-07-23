
import requests
url = "https://api.bithumb.com/public/ticker/all"
data = requests.get(url).json()['data']
#print(data)
str_list = list(data)[0:-1]
print(str_list)

for i in range(len(str_list)):
    opening_price = data[str_list[i]]['opening_price']
    closing_price = data[str_list[i]]['closing_price']
    min_price = data[str_list[i]]['min_price']
    max_price = data[str_list[i]]['max_price']
    change = int(max_price)-int(min_price)
    
    if int(opening_price) + change > int(max_price):
        print("상승장")
    else:
        print("하락장")