#抓取链家数据
import requests
from lxml import etree
from fake_useragent import UserAgent

url='https://hz.lianjia.com/ershoufang/'
headers={'User-Agent':UserAgent().random}

html=requests.get(url=url,headers=headers).content.decode()
p=etree.HTML(html)
list=p.xpath('//li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')

for li in list:
    item={}
    item['title']=li.xpath('.//div[@class="title"]/a/text()')[0].strip()
    item['position']=li.xpath('.//div[@class="positionInfo"]/a[1]/text()')[0].strip()
    item['info']=li.xpath('.//div[@class="houseInfo"]/text()')[0].strip()
    item['totalprice']=li.xpath('.//div[@class="totalPrice"]/span/text()')[0].strip()+'万'
    item['unitprice']=li.xpath('.//div[@class="unitPrice"]/span/text()')[0].strip()
    print(item)