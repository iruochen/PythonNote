# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyQqzhaopinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class QQItem(scrapy.Item):
    '''
    下面定义需要的数据段
    '''
    name = scrapy.Field()
    detailLink = scrapy.Field()
    positionInfo = scrapy.Field()
    workLocation = scrapy.Field()

