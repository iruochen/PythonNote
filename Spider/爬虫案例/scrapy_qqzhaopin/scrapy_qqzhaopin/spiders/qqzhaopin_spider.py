'''
1. 创建项目
2. 编写 item
3. 编写 spider
4. 编写 pipeline
5. 设置 pipeline
'''

import scrapy
import re

from scrapy_qqzhaopin.items import QQItem

class QQSpider(scrapy.Spider):

    name = 'qq'
    # 设置只能爬取腾讯域名信息
    allowed_domains = ['hr.tencent.com']

    start_urls = [
        'https://hr.tencent.com/position.php?&start=0#a'
    ]

    def parse(self, response):

        # 下载的结果自动放在response内存储
        for each in response.xpath('//*[@class="even"]'):
            # 对于得到的每一个工作信息内容
            # 把数据封装入相应的 item 内
            item = QQItem()
            name = each.xpah('./td[1]/a/text()').extract()[0]
            detailLink = each.xpah('./td[1]/a/@href').extract()[0]
            positionInfo = each.xpah('./td[2]/text()').extract()[0]
            workLocation = each.xpah('./td[4]/text()').extract()[0]

            item['name'] = name.encode('utf-8')
            item['detailLink'] = detailLink.encode('utf-8')
            item['positionInfo'] = positionInfo.encode('utf-8')
            item['workLocation'] = workLocation.encode('utf-8')


            # 处理继续爬取的链接
            # 通过得到d当前页，提取数字，把数字加10，替换原来的数字，就是下一页地址
            # 提取当前页的数字
            curpage = re.search('(\d+)', response.url).group(1)
            # 生成下一页的数字值
            page = int(curpage) + 10
            # 生成下一页 url
            url = re.sub('\d+', str(page), response.url)

            # 把地址通过 yield 返回
            # 注意callback 的写法
            yield scrapy.Request(url, callback=self.parse)

            # 获取的item 提交给 Pipeline
            yield item
