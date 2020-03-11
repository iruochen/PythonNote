# with open(fileName, 'wb') as f:
#     f.write()

'''
1. 获取到下载文件的 url，二进制方式下载
urllib，模块提供的 urlretrieve(), 此模块可以进行音频文件下载
        也支持将远程数据下载到本地
urlretrieve(url, filename=None, reporthook=None, data=None)
url: 下载的 url地址
filename: 数据存储路径+文件名
reporthook: 要求回调函数，连接上服务器或者相应数据传输下载完毕时，触发该回调函数
            显示当前的下载进度
data: (filename, headers) 元组
'''

from urllib import request
import requests
import os
from lxml import etree

def Scheduls(blocknum, blocksize, totalsize):
    '''
    显示下载进度
    :param blocknum: 已经下载的数据块
    :param blocksize: 数据块的大小
    :param totalsize: 远程文件大小
    :return:
    '''
    per = 100.0*blocknum*blocksize/totalsize
    if per > 100:
        per = 100
    print('当前下载进度为：{}'.format(per))

url = 'https://www.ivsky.com/bizhi/katong/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'
}

response = requests.get(url, headers=headers)

# print(response.text)
html = etree.HTML(response.text)

# 找到所有的图片链接
img_urls = html.xpath('//div[@class="il_img"]//img/@src')
# print(type(img_urls))

for i in range(len(img_urls)):
    img_urls[i] = 'https:' + img_urls[i]
# print(img_urls)

# print(img_url)
for img_url in img_urls:
    root_dir = 'img'
    if not os.path.exists(root_dir):
        os.mkdir(root_dir)
    filename = img_url.split('/')[-1]
    request.urlretrieve(img_url, root_dir+'/'+filename, Scheduls)
