import requests
from lxml import etree
import os

class Spider(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/80.0.3987.132 Safari/537.36'
        }
        self.offset = 1

    def start(self, url):
        res = requests.get(url, headers=self.headers)
        html = res.text
        html = etree.HTML(html)

        video_srcs = html.xpath('//div[@class="video-play"]/video/@src')
        video_srcs = ['https:' + src for src in video_srcs]
        # print(video_srcs)

        video_titles = html.xpath('//div[@class="show-image"]/img/@alt')
        # print(video_titles)
        self.write_file(video_srcs, video_titles)

    def write_file(self, video_srcs, video_titles):
        for src, title in zip(video_srcs, video_titles):
            response = requests.get(src, headers=self.headers)
            filename = title + '.mp4'
            # print(filename)
            root = 'video'
            if not os.path.exists(root):
                os.makedirs(root)
            with open(root + '\\' + filename, 'wb') as f:
                f.write(response.content)

if __name__ == '__main__':
    spider = Spider()
    urls = ['https://ibaotu.com/shipin/7-0-0-0-0-{}.html'.format(str(i)) for i in range(1, 2)]
    for url in urls:
        spider.start(url)
