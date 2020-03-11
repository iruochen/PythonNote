'''
任务：
爬取斗鱼直播内容
https://www.douyu.com/directory/all
思路：
1. 利用selenium得到页面内容
2. 利用xpath或者bs 等在页面中进行信息提取
'''

from selenium import webdriver
from bs4 import BeautifulSoup
import time

class Douyu():
    # 初始化方法
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "https://www.douyu.com/directory/all"
        print('程序运行中....')

    def douyu(self):
        self.driver.get(self.url)
        self.driver.save_screenshot('page.png')

        while True:
            soup = BeautifulSoup(self.driver.page_source, 'xml')

            # 返回当前页面所有房间标题列表和观众人数
            anchors = soup.find_all('h2', {'class': 'DyListCover-user is-template'})
            titles = soup.find_all('h3', {'class': 'DyListCover-intro'})
            nums = soup.find_all('span', {'class': 'DyListCover-hot is-template'})

            '''
            for title, num in zip(titles, nums):
                print('房间{0} 热度{1}'.format(title.get_text().strip(), num.get_text().strip()))
                '''
            for anchor, title, num in zip(anchors, titles, nums):
                print('主播： {0}  房间标题：{1}  热度：{2}'.format(anchor.get_text().strip(), title.get_text().strip(), num.get_text().strip()))
                with open('douyu.txt', 'a', encoding='utf-8') as f:
                    f.write('主播： {0}  房间标题：{1}  热度：{2}'.format(anchor.get_text().strip(), title.get_text().strip(), num.get_text().strip()) + '\n')


    def destr(self):
        self.driver.quit()

if __name__ == '__main__':
    start_time = time.process_time()
    print('程序开始时间：{}'.format(time.ctime()))
    douyu = Douyu()
    douyu.setUp()
    douyu.douyu()
    douyu.destr()
    end_time = time.process_time()
    print('程序结束时间：{}'.format(time.ctime()))
    print('运行时间：{}'.format(start_time-end_time))