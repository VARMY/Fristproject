import random
import requests

proxy = ['139.208.199.207:8118'
         '123.130.51.220:8118',
         '1.183.152.252:80',
         '121.12.42.91:61234',
         '124.119.93.192:8118',
         '182.46.199.178:8118'
         ]

url = 'http://www.x23us.com/html/41/41345/18593667.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'
}

response = requests.get(url,proxies={'http':random.choice(proxy)},headers=headers)
print(response.text)

