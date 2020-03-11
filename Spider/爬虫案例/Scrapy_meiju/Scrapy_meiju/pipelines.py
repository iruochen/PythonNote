# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class ScrapyMeijuPipeline(object):
    def process_item(self, item, spider):
        return item

class MeijuPipeline(object):
    '''
    此方法必须实现
    用来具体处理 item 内容
    且必须返回一个 item
    '''

    def __init__(self):
        print("init ... meiju.json")
        self.file = open('meiju.json', 'wb')

    def process_item(self, item, spider):
        '''
        此案例只是把 item 值打印出来
        :param item:
        :param spider:
        :return:
        '''

        print(item['name'])

        with open('meiju.json', 'a', encoding='utf-8') as f:
           json.dump(dict(item), f, ensure_ascii=False) + '\n'

        return item

    def close_spider(self):
        self.file.close()