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
import csv

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
    rows = []
    for i in range(1, int(page+1)):
        time.sleep(2)
        url = 'https://so.csdn.net/so/search/s.do?p={1}&q={0}&t=blog&viparticle=&domain=&o=&s=&u=&l=&f=&rbg=0'.format(key, i)
        # print(url)
        res = request_get(url)
        html = etree.HTML(res)
        # 获取文章链接
        article_base_urls = html.xpath('//div[@class="search-list-con"]/dl/dt/div/a/@href')
        # 去重
        article_urls = list(set(article_base_urls))
        # print(len(article_urls))
        count = 0
        for article_url in article_urls:
            count = count + 1
            # print(article_url)
            res = request_get(article_url)
            html = etree.HTML(res)
            # 获取文章标题
            title = html.xpath('//h1/text()')[0]
            # print(title)
            # 获取文章作者
            author = html.xpath('//a[@class="follow-nickName"]/text()')[0]
            # print(author)
            # 获取文章发布时间
            base_date = html.xpath('//span[@class="time"]/text()')[0]
            # print(base_time)
            date = re.findall(r'(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2})', base_date)[0]
            # print(time)
            # 获取阅读数
            readCount = html.xpath('//span[@class="read-count"]/text()')[0]
            readCount = re.findall(r'\d+', readCount)[0]
            # print(readCount)
            # 获取正文
            content = (title, article_url, author, date, readCount)
            rows.append(content)
            print('第 {} 页 --- 第 {} 篇文章爬取完成'.format(i, count))
        print('-'*20)
        print('第 {} 页爬取完成'.format(i))
        print('-'*20)
    return rows


def to_csv(headers, rows):
    with open('article.csv', 'a', encoding='utf-8', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)


if __name__ == '__main__':
    headers = ['title', 'link', 'author', 'time', 'readCount']
    to_csv(headers, get_url('java', 10))
    print('write success')
