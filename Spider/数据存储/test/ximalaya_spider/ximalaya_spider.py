'''
喜马拉雅音乐下载
pip install pypinyin  # 将中文解析成对应的拼音
'''
import requests
from pypinyin import lazy_pinyin
import re
import json, os
from urllib import request
import socket
socket.setdefaulttimeout(30)

# 翻译查找的歌曲类型
def fanyi(string):
    var = lazy_pinyin(string)
    str = ''.join(var)
    return str

# 获取详情页面信息
def get_page(str, headers):
    url = 'https://www.ximalaya.com/yinyue/{}/'.format(str)
    # print(url)
    res = requests.get(url, headers=headers)
    html = res.text
    return url, html

# {"albumId":27888315,"title":"3D大自然睡前曲|枕着宇宙万物入眠 立体声无损享受"
# 获取albumId值
# albumId值已经不可以直接获取歌曲目录
# 先通过拼接网站访问，再获取歌曲目录
def get_albumId(html):
    albumIds = re.findall(r'"albumId":(\d{2,}),', html)
    # albumId = albumIds[:1][0]
    # print(albumId)
    # 构建下载地址
    # url = 'https://www.ximalaya.com/revision/play/v1/show?id={}&sort=0&size=30&ptype=1'.format(albumId)
    return albumIds

def get_trackId(hraders, url, albumIds):
    # for albumId in albumIds:
    # albumId = albumIds[:0][0]
    albumIds = list(set(albumIds))
    # print(albumIds)
    # print(len(albumIds))
    albumId = albumIds[:1][0]
    music_ID = []
    for albumId in albumIds:
        link = url + albumId
        html = requests.get(link, headers=headers).text
        pattern = re.compile(r'"trackId":(\d+)')
        trackId = pattern.search(html)
        if trackId:
            trackId = trackId.group(0).split(':')[-1]
            music_url = link + '/' + trackId
            # print(music_url)
            music_html = requests.get(music_url, headers=headers).text
            datas = re.findall(r'"trackId":(\d{2,}),"title":"(.*?)",', music_html)
            for data in datas:
                music_ID.append(data)
    return music_ID

def downloads(headers, music_ID):
    root = 'music'
    if not os.path.exists(root):
        os.makedirs(root)
    try:
        for music in music_ID:
            trackId = music[0]
            title = music[1]
            url = 'https://www.ximalaya.com/revision/play/v1/audio?id={}&ptype=1'.format(trackId)
            res = requests.get(url, headers=headers).text
            html = json.loads(res)
            src = html['data']['src']
            base = '.m4a'
            if '/' in title:
                title = title.replace('/', '-')
            try:
                print('正在下载{}'.format(title))
                filename = root + '\\' + title + '.mp3'
                if base in src and src != None:
                    request.urlretrieve(src, filename)
                    print('下载完成～～～')
            except socket.timeout:
                print('{}下载失败'.format(title))
    except:
        pass

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/80.0.3987.132 Safari/537.36'
    }
    music_type = input('please input your music type: ')
    str = fanyi(music_type)
    url, html = get_page(str, headers)
    albumIds = get_albumId(html)
    music_ID = get_trackId(headers, url, albumIds)
    downloads(headers, music_ID)
