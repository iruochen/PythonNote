import requests
from lxml import etree
# from .hupu_mongo import MongoAPI
from Spider.数据存储.test.hupu_spider.hupu_mongo import MongoAPI
import time


# 获取初始页面信息
def spider(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/80.0.3987.132 Safari/537.36'
    }

    # 请求页面
    res = requests.get(url, headers=headers)
    html = res.text
    # print(html)
    html = etree.HTML(html)
    return html

# 解析页面内容
def parse(html):
    # 获取标题 方法一
    titles = html.xpath('//ul[@class="for-list"]//div[@class="titlelink box"]/a[@class="truetit"]//text()')
    # print(titles)

    # 获取详情页面链接信息
    parse_hrefs = html.xpath('//ul[@class="for-list"]//div[@class="titlelink box"]/a[@class="truetit"]/@href')
    parse_hrefs = ['https://bbs.hupu.com' + href for href in parse_hrefs]
    # print(parse_hrefs)

    '''
    # 获取标题 方法二
    titles_2 = []
    for href in parse_hrefs:
        titles_2.append(title(href))
    print(titles_2)
    '''

    # 获取作者
    authors = html.xpath('//div[@class="author box"]/a[@class="aulink"]/text()')
    # print(authors)
    # 获取作者主页链接
    author_links = html.xpath('//div[@class="author box"]/a[@class="aulink"]/@href')
    # print(author_links)

    # 获取发布时间
    article_times = html.xpath('//div[@class="author box"]/a[2]/text()')
    # print(article_times)

    # 获取回复数和浏览数
    datas = html.xpath('//ul[@class="for-list"]/li/span[@class="ansour box"]/text()')
    # print(datas)
    datas = [x.split('\xa0/\xa0') for x in datas]
    # print(datas)

    # 获取回复数
    replies = [x[0] for x in datas]
    # 浏览数
    browses = [x[1] for x in datas]
    # print(replies)
    # print(browses)

    # 最后回复时间
    last_times = html.xpath('//div[@class="endreply box"]/a/text()')
    # print(last_times)
    # 最后回复人
    last_names = html.xpath('//div[@class="endreply box"]/span[@class="endauthor "]/text()')
    # print(last_names)

    # print(titles)
    # print(parse_hrefs)
    # print(authors)
    # print(author_links)
    # print(article_times)
    # print(replies)
    # print(browses)
    # print(last_times)
    # print(last_names)
    # print(len(titles), len(parse_hrefs), len(authors), len(author_links), len(article_times),
    #       len(replies), len(browses), len(last_times), len(last_names))

    items = zip(titles, parse_hrefs, authors, author_links, article_times, replies, browses, last_times, last_times)
    return items

# 数据存储
def data_storage(items):
    hupu_post = MongoAPI('127.0.0.1', 27017, 'hupu', 'data')
    for item in items:
        hupu_post.add({
            'title': item[0],
            'parse_href': item[1],
            'author': item[2],
            'author_link': item[3],
            'article_time': item[4],
            'reply': item[5],
            'browse': item[6],
            'last_time': item[7],
            'last_name': item[8]
        })
    print('写入完成')

'''
def title(href):
    html = spider(href)
    title = html.xpath('//div[@class="bbs-hd-h1"]/h1/text()')
    return title
'''

def main():
    num = 1
    urls = ['https://bbs.hupu.com/nba-{}'.format(str(i)) for i in range(1, 11)]
    for url in urls:
        time.sleep(2)
        print('正在爬取第{}页数据, 请耐心等待 ～～～'.format(num))
        num = num + 1
        html = spider(url)
        data_storage(parse(html))
    print('爬取完成，共爬取{}页数据'.format(num))


if __name__ == '__main__':
    main()
