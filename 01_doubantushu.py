#https://book.douban.com/top250?start=0/25/50/....
import requests
from lxml import etree
import time
import random
from fake_useragent import UserAgent

class TUSHU:
    def __init__(self):
        self.url='https://book.douban.com/top250?start={}'

    
    def get_html(self,url):
        """使用随机的User-Agent"""
        headers={
            'User-Agent':UserAgent().random
        }
        html=requests.get(url=url,headers=headers).content.decode('utf8','ignore')
        self.lxml_html(html)
    
    def lxml_html(self,html):
        """lxml+xpath进行数据解析"""
        #解析函数
        #1.解析对象
        l_html=etree.HTML(html)
        #2.生成节点对象--基准xpath
        l_list=l_html.xpath('//div[@class="indent"]/table')
        #3.提取节点对象数据
        for l in l_list:
            item={}
            #判断是否为空
            if l.xpath('.//div[@class="pl2"]/a/text()'):
                item['name']=l.xpath('.//div[@class="pl2"]/a/text()')[0].strip()
            else:
                item['name']=None
            if l.xpath('.//p[@class="pl"]/text()'):
                item['info']=l.xpath('.//p[@class="pl"]/text()')[0].strip()
            else:
                item['info']=None
            if l.xpath('.//span[@class="rating_nums"]/text()'):
                item['score']=l.xpath('.//span[@class="rating_nums"]/text()')[0].strip()
            else:
                item['info']=None
            if l.xpath('.//span[@class="pl"]/text()'):
                item['nums']=l.xpath('.//span[@class="pl"]/text()')[0].split('\n')[1].strip()
            else:
                item['info']=None
            if l.xpath('.//span[@class="inq"]/text()'):
                item['inq']=l.xpath('.//span[@class="inq"]/text()')[0].strip()
            else:
                item['info']=None
            

            print(item)
        
    def run(self):
        for i in range(10):
            page_url=self.url.format(i*25)
            self.get_html(url=page_url)
            time.sleep(random.randint(2,3))

if __name__ == "__main__":
    TUSHU().run()

