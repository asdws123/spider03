#建立代理ip池
#1.获取代理ip
#2.依次测试，能用的保存到mysql数据库

import requests
import time

class ProxyPool:
    def __init__(self):
        self.url=''
        self.headers={'User-Agent':''}
        #self.name=
        #self.sercet=
    
    def get_proxy(self):
        #获取代理ip
        html=requests.get(url=self.url,headers=self.headers).content.decode('utf8','ignore')
        #分割结果
        list=html.split('\r\n')
        #依次测试
        for proxy in list:
            self.test_proxy(proxy)
    
    def test_proxy(self,proxy):
        #测试代理ip是否可用函数
        test_url='http://httpbin.org/get'
        proxies={
            #开放代理
            'http':'http://{}'.format(proxy),
            'https':'https://{}'.format(proxy)
            #私密代理/独享代理
            #'http':'http://self.name:self.sercet@{}'.format(proxy),
            #'https':'https://self.name:self.sercet@{}'.format(proxy)
        }
        try:
            res=requests.get(url=test_url,proxies=proxies,timeout=2)
            #响应状态码
            if res.status_code==200:
                print(' %s is ok '%proxy)
        except :
            print(' %s is not ok '%proxy)

    def run(self):
        self.get_proxy()

if __name__ == "__main__":
    ProxyPool().run()