'''
url: https://so.csdn.net/so/search/s.do?q=java&t=blog&o=&s=&l=&f=&viparticle=
分析链接，容易发现 q = ()  是搜索内容
我们改变关键词为c，访问成功
点击下一页
url: https://so.csdn.net/so/search/s.do?p=2&q=java&t=blog&viparticle=&domain=&o=&s=&u=&l=&f=&rbg=0
分析链接
改变p=.... 即可改变页数
'''
import requests
import os, time, re
import random
from lxml import etree

def request_get(url):
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
        ' Chrome/80.0.3987.122 Safari/537.36'
    ]
    headers = {
        'User-Agent': random.choice(user_agent_list)
    }

    try:
        response = requests.get(url, headers=headers)
        return response.text
    except Exception as e:
        print(e)


def get_url(key, page):
    for i in range(1, int(page+1)):
        url = 'https://so.csdn.net/so/search/s.do?p={1}&q={0}&t=blog&viparticle=&domain=&o=&s=&u=&l=&f=&rbg=0'.format(key, i)
        print(url)
        res = request_get(url)
        html = etree.HTML(res)
        # 获取文章链接
        article_base_urls = html.xpath('//div[@class="search-list-con"]/dl/dt/div/a/@href')
        # 去重
        article_urls = list(set(article_base_urls))
        # print(len(article_urls))
        for article_url in article_urls:
            print(article_url)
            res = request_get(article_url)
            html = etree.HTML(res)
            # 获取文章标题
            title = html.xpath('//h1/text()')[0]
            # print(title)
            # 获取文章作者
            author = html.xpath('//a[@class="follow-nickName"]/text()')[0]
            # print(author)
            # 获取文章发布时间
            base_time = html.xpath('//span[@class="time"]/text()')[0]
            # print(base_time)
            time = re.findall(r'(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2})', base_time)[0]
            # print(time)
            # 获取阅读数
            readCount = html.xpath('//span[@class="read-count"]/text()')[0]
            readCount = re.findall(r'\d+', readCount)[0]
            # print(readCount)
            # 获取正文

if __name__ == '__main__':
    get_url('c', 1)