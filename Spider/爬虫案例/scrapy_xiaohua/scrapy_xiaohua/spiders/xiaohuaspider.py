'''
校花网貌似已经凉了

1. 创建项目
2. 编写item
3. spider
4. pipeline
5. 设置pipeline
6. 中间件，会使用selenium
'''
import scrapy
from urllib import request

from scrapy_xiaohua.items import XiaohuaItem

class XiaohuaSpider(scrapy.Spider):

    name = 'xiaohua'
    allowed_domains = ['xiaohua100.cn']

    start_urls = ['http://xiaohua100.cn']

    def parse(self, response):

        bookmarks = response.xpath('//div[@data-uid="1"]')
        for bm in bookmarks:
            item = XiaohuaItem()

            title = bm.xpath('.//h3/span[@class="cellTir"]/a/text()').extract()[0]
            href = bm.xpath('.//h3/span[@class="cellTir"]/a/@href').extract()[0]
            src = bm.xpath('.//div[@class="pic"]/a/img/@src').extract()[0]

            item['title'] = title
            item['href'] = request.urljoin(response.url, href)
            item['src'] = request.urljoin(response.url, src)

            yield item

