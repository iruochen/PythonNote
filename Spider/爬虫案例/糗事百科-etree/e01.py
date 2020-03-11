'''
糗事百科已凉。。。 默哀。。
翻车。。。
爬取糗事百科
分析：
1. 需要用到requests爬取页面，用xpath、re来提取数字
2. 可提取信息 用户头像链接，段子内容，点赞，好评次数
3. 保存到json文件中

流程：
1. down下页面
2. 利用xpath提取信息
3. 保存文件落地
'''

import requests
from lxml import etree

url = "https://www.qiushibaike.com/8hr/page/1/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}

# 下载页面
try:
    rsp = requests.get(url, headers=headers)
    html = rsp.text
except Exception as e:
    print(e)

# 把页面解析成html
html = etree.HTML(html)
rst = html.xpath('//div[contains(@id, "qiusi_tag")]')

for r in rst:
    item = {}

    content = r.xpath('//div[@class="content]/span')[0].text.strip()
    print(content)
