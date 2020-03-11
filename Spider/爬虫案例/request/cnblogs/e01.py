import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.100 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'cache-control': 'max-age=0'
}

url = 'https://www.cnblogs.com/cate/python/'
html = requests.get(url, headers=headers)

# print(html.text)

soup = BeautifulSoup(html.text, 'lxml')

items = soup.select('div[class="post_item_body"]')
# print(items)
for item in items:
    # 标题
    title = item.select('h3 a[class="titlelnk"]')[0].get_text()
    # print(title)
    # 详情链接
    href = item.select('h3 a[class="titlelnk"]')[0].get('href')
    # href = item.select('h3 a[class="titlelnk"]')[0]['href']
    # print(href)
    # 作者
    author = item.select('div[class="post_item_foot"] a')[0].get_text()
    # print(name)
    # 作者博客主页链接
    author_home = item.select('div[class="post_item_foot"] a')[0]['href']
    # print(author + ' -- ' + author_home)
    # 简要信息
    infos = item.select('p[class="post_item_summary"]')[0].get_text().strip('\n').strip(' ').strip('\r\n')
    # print(infos)
    datas = item.select('div[class="post_item_foot"]')[0].get_text()
    # print(datas)
    datas = datas.split(' ')
    # print(datas, type(datas))
    # 发布时间
    time = datas[6] + ' ' + datas[7]
    # print(time)
    # 评论数
    comment = datas[-1].lstrip('评论(').strip(')')[0]
    # print(comment)
    # 阅读数
    read_num = datas[-1].lstrip('阅读(').rstrip(')').strip('(')[-1]
    # print(read_num)

