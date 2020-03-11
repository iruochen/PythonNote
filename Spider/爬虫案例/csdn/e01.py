import requests
import random
from lxml import etree
import os, time, re

def request_get(url):
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
        ' Chrome/80.0.3987.122 Safari/537.36'
    ]
    headers = {
        'User-Agent': random.choice(user_agent_list)
    }

    try:
        response = requests.get(url, headers=headers)
        return response
    except Exception as e:
        print(e)


def get_article_topics(url):
    '''
    获取文章主题
    :param url:
    :return:
    '''
    res = request_get(url)
    html = etree.HTML(res.text)
    # 获取文章主题链接
    article_topic_urls = html.xpath('//div[@class="container clearfix"]/nav/div/div/ul/li/a/@href')
    # 删除多余项
    article_topic_urls.remove('https://blockchain.csdn.net')
    article_topic_urls.remove('https://ai.csdn.net')
    article_topic_urls.remove('https://cloud.csdn.net/')
    del article_topic_urls[1]
    return article_topic_urls

def get_article(url, topic):
    '''
    获取文章链接
    :param url:
    :param topic:
    :return:
    '''
    # 拼接文章主题链接
    base_url = url + topic
    # print(base_url)
    req = request_get(base_url)
    article_html = etree.HTML(req.text)
    # 获取文章链接
    article_links = article_html.xpath('//ul[@id="feedlist_id"]/li/div/div/h2/a/@href')
    return article_links

def get_article_info(url):
    req = request_get(url)
    html = etree.HTML(req.text)
    # 获取文章标题
    title = html.xpath('//h1[@class="title-article"]/text()')[0].strip()
    # 获取文章正文
    contents = html.xpath('//div[@id="content_views"]/p/text()')
    # 获取文章图片链接
    pic_base_urls = html.xpath('//div[@id="article_content"]/div[@class="htmledit_views"]/p/img/@src')

    title = title.replace('*', '').replace('|', '').replace('；', '').replace('：', '').replace(' ', '')\
        .replace('/', '').replace('/', '').replace('!', '').replace(':', '').replace('?', '')
    root = 'csdn_article'
    folder_name = title
    path = root + '\\' + folder_name
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except:
            pass
    # 写入文件
    for content in contents:
        downloader_article(path, title, content)

    pic_urls = []
    for pic_base_url in pic_base_urls:
        # 去除图片水印
        pic_url = pic_base_url.split('?')[-1]
        pic_urls.append(pic_url)

    for pic_url in pic_urls:
        img_name = pic_url.split('/')[-1]
        downloader_pic(pic_url, path, img_name)


# 下载文章
def downloader_article(path, filename, text):
    try:
        with open(path+'\\'+filename+'.txt', 'a', encoding='utf-8') as f:
            f.write(text + '\n')
    except Exception as e:
        print(e)

# 下载图片
def downloader_pic(pic_url, path, img_name):
    try:
        res = request_get(pic_url)
        with open(path+'\\'+img_name, 'wb') as f:
            f.write(res.content)
    except:
        pass

count = 0

def spider():
    print('程序运行中....')
    global count
    url = 'https://www.blog.csdn.net'
    for topic in get_article_topics(url):
        for article_url in get_article(url, topic):
            time.sleep(2)
            get_article_info(article_url)
            count = count + 1
            print('Waiting..................')
        print('topic: ' + topic + '下载结束～～～')
        print('-'*20)

    print('共下载 ' + str(count) + '篇文章')


if __name__ == '__main__':
    spider()
    '''
    url = 'https://www.csdn.net'
    for topic in get_article_topics(url):
        print('topic: ', topic)
        print(get_article(url, topic))
        print('--'*20)
        '''
