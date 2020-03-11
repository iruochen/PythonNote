'''
利用最简单的爬虫
爬取百度页面
关闭配置机器人地址

要求导入scrapy
所有类一般是 xxxSpider 命名
所有爬虫类是 scrapy.Spider 的子类

命令：
svrapy startproject baidu
scrapy crawl baidu
'''

import scrapy

class BaiduSpider(scrapy.Spider):

    # name 是爬虫的名称
    name = 'baidu'

    # 起始 url 列表
    start_urls = ['http://www.baidu.com']

    # 负责分析 downloader 下载得到的结果
    def parse(self, response):
        '''
        只是保存网页即可
        :param response:
        :return:
        '''
        with open('baidu.html', 'w', encoding='utf-8') as f:
            f.write(response.body.decode('utf-8'))