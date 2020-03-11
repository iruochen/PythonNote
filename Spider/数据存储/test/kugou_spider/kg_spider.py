'''
库狗音乐top500 抓取

url = https://www.kugou.com/yy/rank/home/1-8888.html?from=homepage
页面信息
    1 - 23   500

最终数据存储至mongodb
'''

import requests
from bs4 import BeautifulSoup
import time
from pymongo import MongoClient

client = MongoClient()
songs = client.kugou_db.songs

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/80.0.3987.132 Safari/537.36'
}
def kg_spider(url):
    '''
    获取库狗音乐top500，保存至mongodb
    :param url: 请求地址
    :return:
    '''
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')

    ranks = soup.select('.pc_temp_num')
    # print(ranks)
    titles = soup.select('.pc_temp_songlist > ul > li > a')
    # print(titles)
    times = soup.select('.pc_temp_time')
    # print(times)
    for rank,title,time in zip(ranks, titles, times):
        # 歌曲编号
        rank = rank.get_text().strip()
        # print(rank)
        # 歌曲名称
        song = title.get_text().split('-')[-1].strip()
        # print(song)
        # 歌手
        singer = title.get_text().split('-')[0].strip()
        # print(singer)
        # 歌曲时长
        songTime = time.get_text().strip()
        # print(songTime)
        # print(rank, song, singer, songTime)

        data = {
            'rank': rank,
            'singer': singer,
            'song': song,
            'time': songTime
        }
        songs_id = songs.insert(data)
        print(songs_id)

if __name__ == '__main__':
    urls = ['https://www.kugou.com/yy/rank/home/{}-8888.html?from=homepage'.format(str(i)) for i in range(1, 24)]
    for url in urls:
        kg_spider(url)
        time.sleep(1)

