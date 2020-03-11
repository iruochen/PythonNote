# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyMeijuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MeijuItem(scrapy.Item):
    name = scrapy.Field()
    href = scrapy.Field()
    tv = scrapy.Field()
    state = scrapy.Field()
    time = scrapy.Field()
