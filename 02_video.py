from fake_useragent import UserAgent
from lxml import etree
import requests

# url=https://tieba.baidu.com/p/7016979395
url='https://tieba.baidu.com/p/7016979395'
headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

html=requests.get(url=url,headers=headers).content.decode()
p=etree.HTML(html)
#此处响应内容和前端检查元素不一致
list=p.xpath('//div[@class="video_src_wrapper"]/embed /@data-video')
src=list[0]

#保存视频
video_html=requests.get(url=src,headers=headers).content
with open('kasa.mp4','wb') as f:
    f.write(video_html)