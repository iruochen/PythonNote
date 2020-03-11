import re
from urllib import request
import json

def get_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    }
    req = request.Request(url, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    return html

def parse_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?title="(.*?)".*?<img.*?data-src="(.*?)".*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S
    )
    items = pattern.findall(html)
    for item in items:
        yield {
            "index": item[0],
            "title": item[1],
            "image": item[2],
            "stars": item[3],
            "relaeasetime": item[4],
            "score": item[5] + item[6]
        }

def write_to_file(content):
    # a: 只写模式
    with open('top10.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')

if __name__ == '__main__':
    print("starting....")
    url = "http://maoyan.com/board"
    html = get_page(url)
    for item in parse_page(html):
        write_to_file(item)
    print("ending....")
