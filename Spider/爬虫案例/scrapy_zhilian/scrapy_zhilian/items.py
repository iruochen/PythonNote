# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyZhilianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ZhilianItem(scrapy.Item):
    job_name = scrapy.Field()
    company_name = scrapy.Field()
    company_link = scrapy.Field()
    advantage = scrapy.Field()
    salary = scrapy.Field()
    place = scrapy.Field()
    post_time = scrapy.Field()
    job_nature = scrapy.Field()
    work_experience = scrapy.Field()
    education = scrapy.Field()
    job_number = scrapy.Field()
    job_kind = scrapy.Field()
    job_des = scrapy.Field()
    company_des = scrapy.Field()
    url = scrapy.Field()

