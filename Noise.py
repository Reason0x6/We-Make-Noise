from itertools import cycle
from lxml.html import fromstring
import requests
import datetime
import time
import random 


print(" __       __                  __       __            __                        __    __            __                     ")
print("|  \  _  |  \                |  \     /  \          |  \                      |  \  |  \          |  \                    ")
print("| $$ / \ | $$  ______        | $$\   /  $$  ______  | $$   __   ______        | $$\ | $$  ______   \$$  _______   ______  ")
print("| $$/  $\| $$ /      \       | $$$\ /  $$$ |      \ | $$  /  \ /      \       | $$$\| $$ /      \ |  \ /       \ /      \ ")
print("| $$  $$$\ $$|  $$$$$$\      | $$$$\  $$$$  \$$$$$$\| $$_/  $$|  $$$$$$\      | $$$$\ $$|  $$$$$$\| $$|  $$$$$$$|  $$$$$$\ ")
print("| $$ $$\$$\$$| $$    $$      | $$\$$ $$ $$ /      $$| $$   $$ | $$    $$      | $$\$$ $$| $$  | $$| $$ \$$    \ | $$    $$")
print("| $$$$  \$$$$| $$$$$$$$      | $$ \$$$| $$|  $$$$$$$| $$$$$$\ | $$$$$$$$      | $$ \$$$$| $$__/ $$| $$ _\$$$$$$\| $$$$$$$$")
print("| $$$    \$$$ \$$     \      | $$  \$ | $$ \$$    $$| $$  \$$\ \$$     \      | $$  \$$$ \$$    $$| $$|       $$ \$$     \ ")
print("\$$      \$$  \$$$$$$$       \$$      \$$  \$$$$$$$ \$$   \$$  \$$$$$$$       \$$   \$$  \$$$$$$  \$$ \$$$$$$$   \$$$$$$$")
print("") 

#User Agents to make you look like a human
useragents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57',
    'Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.1.4322)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2)',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'    
    ]



#Get list of proxys to attempt to use
def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr'):
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            #Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies

#proxies Example = ['121.129.127.209:80', '124.41.215.238:45169', '185.93.3.123:8080', '194.182.64.67:3128', '106.0.38.174:8080', '163.172.175.210:3128', '13.92.196.150:8080']
proxies = get_proxies()
proxy_pool = cycle(proxies)

for i in range(11,len(proxies)):
    #Get a proxy from the pool
    proxy = next(proxy_pool)
    print("Request #%d"%i)
    try:
        j = i % len(useragents)
        headers = {
            'Host': 'localhost:80',
            'Connection': 'close',
            'Content-Length': '64',
            'Accept': '*/*',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': useragents[j],
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://localhost:8080',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'google.com',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }
        if i % random.randint(50,67) == 1:
            data = 'user=cb09c6ce689c750a&UUID=31e9d0e8cb830513&projdelta=70971c58=='
        else:
            data = 'user=d98b02b57ff3b63f&UUID=f3570503a8867c25&projdelta=e580184bae'

        response = requests.post('localhost:80/formsub', headers=headers, data=data, verify=False,proxies={"http": proxy, "https": proxy})

        print(response.json())
        
    except:
       pass

    rand = random.randint(1,1380)
        

    timer = datetime.datetime.now()

    current_time = timer + datetime.timedelta(0,rand)
    print("Next Attempt Time =", current_time.strftime("%H:%M:%S"))

    time.sleep(rand)


    
