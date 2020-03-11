'''
利用正则来爬取猫眼电影
1. url: http://maoyan.com/board
2. 把电影信息尽可能多的拿下来

分析：
1. 一个影片的内容是以dd开头的单元
2. 在单元内存在一部电影的所有信息

思路：
1. 利用re把dd内容都给找到
2. 对应找到的每一个dd，用re挨个搜查需要的信息

方法就是三步走：
1. 把页面down下来
2. 提取出dd单元为单位的内容
3. 对每一个dd，进行单独信息提取
'''

from urllib import request

# 1. 下载页面内容
url = "http://maoyan.com/board"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}

req = request.Request(url, headers=headers)
rsp = request.urlopen(req)

html = rsp.read().decode()

# 2. 按dd提取出内容来，缩小处理范围
import re

s = r'<dd>(.*?)</dd>'

pattern = re.compile(s, re.S)

films = pattern.findall(html)
# 3. 从每一个dd中单独提取出需要的信息
for film in films:
    # 提取电影名称
    s = r'<a.*?title="(.*?)"'
    pattern = re.compile(s, re.S)
    title = pattern.findall(film)[0]
    print(title)

    # 提取index
    s = r'board-index.*?>(.*?)</i>.*?'
    pattern = re.compile(s)
    index = pattern.findall(film)[0]
    # print(index)

    # 提取img
    s = r'<img.*?data-src="(.*?)"'
    pattern = re.compile(s)
    img = pattern.findall(film)[0]
    # print(img)

    # 提取star
    s = r'.*?star">(.*?)</p>'
    # 此处必须加re.S
    # 不加re.S, 默认只在一行进行匹配，找不到star
    pattern = re.compile(s, re.S)
    star = pattern.findall(film)
    # print(star)

    # 提取上映时间
    s = r'.*?releasetime">(.*?)</p>'
    pattern = re.compile(s)
    releasetime = pattern.findall(film)
    # print(releasetime)

    # 爬取评分
    s = r'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>'
    pattern = re.compile(s)
    num = pattern.findall(film)
    # print(num)
    # 至此，我们需要的大部分信息已经提取完毕

