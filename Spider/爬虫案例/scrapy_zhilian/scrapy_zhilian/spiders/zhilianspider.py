import scrapy
from scrapy_zhilian.items import ZhilianItem

class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    allowed_domains = ['zhaopin.com']
    start_urls = ['http://sou.zhaopin.com/jobs/searchresult.ashx?j1=北京&kw=python']

    def parse(self, response):

        print('URL_PAGE: {0}'.format(response.url))

        nextUrls = response.xpath('//li[@class="pagesDown-pos"]/a/@href').extract()
        for url in nextUrls:
            if len(url) > 5:
                yield scrapy.Request(url)

        job_urls = response.xpath('//')