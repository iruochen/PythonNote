import requests, json
from bs4 import BeautifulSoup

url =  'http://www.seputu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.100 Safari/537.36'
}

html = requests.get(url, headers=headers)

soup = BeautifulSoup(html.text, 'lxml')
content = []
for mulu in soup.find_all(class_='mulu'):
    # 标题
    h2 = mulu.find('h2')
    if h2 != None:
        h2_title = h2.string    # 获取标题
        # print(h2_title)
        list = []
        # 获取章节内容与url地址
        for a in mulu.find(class_='box').find_all('a'):
            href = a.get('href')
            box_title = a.get('title')
            # print(href, box_title)
            list.append({'href': href, 'box_title': box_title})
        content.append({'title': h2_title, 'content': list})

with open('ghd.json', 'a', encoding='utf-8') as fp:
    json.dump(content, fp=fp, indent=4, ensure_ascii=False)
