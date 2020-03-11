# from pypinyin import lazy_pinyin
#
# a = '若尘'
# print(lazy_pinyin(a))
# b = lazy_pinyin(a)
# b = ''.join(b)
# print(b)

import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/80.0.3987.132 Safari/537.36'
}

url = 'https://www.ximalaya.com/yinyue/249689/'
html = requests.get(url, headers=headers).text
pattern = re.compile(r'"trackId":(\d{2,})')
s = pattern.search(html)
s = s.group(0).split(':')[-1]
# print(s.group(0).split(':')[-1])

url = url + s
# print(url)
html = requests.get(url, headers=headers).text
# print(html)
m = re.findall(r'"trackId":(\d{2,}),"title":"(.*?)",', html)
for i in m:
    print(i)
