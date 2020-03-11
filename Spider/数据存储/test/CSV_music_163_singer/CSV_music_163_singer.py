'''
网易云音乐歌手信息抓取
url = https://music.163.com/discover/artist/cat?id=4001&initial=0

id=4001    id: 歌手类别
initial=0
initial = [-1. 65-90, 0]
'''
import requests
from bs4 import BeautifulSoup
import csv
import time

def get_artist(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/69.0.3497.100 Safari/537.36',
        'Referer': 'https://music.163.com/',
        'Host': 'music.163.com'
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    items = soup.find_all('a', attrs={'class': 'nm nm-icn f-thide s-fc0'})
    for item in items:
        artist_name = item.string.strip()
        artist_id = item['href'].replace('/artist?id=', '').strip()
        # print(artist_id, artist_name)
        try:
            writer.writerow((artist_id, artist_name))
        except Exception as e:
            print('写入失败 ～ ～ ～')
            print(e)

if __name__ == '__main__':
    print('程序运行中 ～ ～ ～')
    start_time = time.process_time()
    id_list = [1001, 1002, 1003, 2001, 2002, 2003, 6001, 6002, 6003,7001, 7002, 7003, 4001, 4002, 4003]
    initial_list = [-1, 0]
    a = [x for x in range(65, 91)]
    initial_list.extend(a)

    # 文件存储位置
    csvfile = open('music_163_artist.csv', 'a', encoding='utf-8', newline='')
    writer = csv.writer(csvfile)
    writer.writerow(('artist_id', 'artist_name'))

    for i in id_list:
        for j in initial_list:
            url = 'https://music.163.com/discover/artist/cat?id={}&initial={}'.format(i, j)
            # print(url)
            get_artist(url)

    end_time = time.process_time()
    print('程序运行时间：', start_time-end_time)