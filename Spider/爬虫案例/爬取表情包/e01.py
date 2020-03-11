'''
url = http://www.doutula.com/search?type=photo&more=1&keyword=%E6%80%BC%E4%BA%BA&page=1
很容易拼接
'''

import requests
import os
from lxml import etree


url = 'http://www.doutula.com/search?type=photo&more=1&keyword=%E6%80%BC%E4%BA%BA&page=1'
res = requests.get(url)
html = etree.HTML(res.text)
pic_urls = html.xpath('//div[@class="random_picture"]/a/img/@data-original')
names = html.xpath('//div[@class="random_picture"]/a/p/text()')

for pic_url in pic_urls:
    try:
        root_dir = 'doutu'
        if not os.path.exists(root_dir):
            os.mkdir(root_dir)
        # file_name = name.replace('')
        pic = requests.get(pic_url)
        # file_name = name + '.gif'
        file_name = pic_url.split('/')[-1]
        with open(root_dir + '\\' + file_name, 'wb') as f:
            f.write(pic.content)

    except Exception as e:
        print(e)

print('下载完成～～～')

