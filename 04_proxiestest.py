#使用代理IP访问测试网站

import requests

url=' http://httpbin.org/get'
headers={'User-Agent':'Mozilla/5.0'}
proxies={
    'http':'http://49.87.72.191:9999',
    'https':'https://49.87.72.191:9999'
}

html=requests.get(url=url,proxies=proxies,headers=headers).text

print(html)