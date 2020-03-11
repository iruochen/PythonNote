import requests
from lxml import etree
import os, time
from functools import wraps

def f(urls):
    def down_url(func):
        @wraps(func)
        def inner(*args):
            headers = {
                'User-Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64;rv: 72.0) Gecko / 20100101Firefox / 72.0',
                'Referer': 'http://www.mzitu.com'
            }
            for url in urls:
                res = requests.get(url, headers=headers)
                html = etree.HTML(res.text)
                yield func(html)
        return inner
    return down_url

urls = ['http://www.mzitu.com']
@f(urls)
def get_url(html):
    img_src = html.xpath('//div[@class="postlist"]/ul/li/a/@href')
    print(img_src)
    return img_src

'''
def img_prase(img_src):
    for img_url in img_src:
        @f(img_url)
        def pic(html):
            # 获取标题
            title = html.xpath('//div[@class="content"]/h2/text()')[0]
            print(title)

'''

if __name__ == '__main__':
    get_url()
