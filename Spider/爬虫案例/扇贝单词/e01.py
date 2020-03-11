'''
扇贝单词：
1. 把python单词列表download下来
2. 主要练习目的是xpath
3. 理论上不需要登陆
4. url = "https://www.shanbay.com/wordlist/104899/202159"
'''
from urllib import request
from lxml import etree
import json
import time

def get_page(page):
    url = "https://www.shanbay.com/wordlist/104899/202159?page=%s"%page
    headers = {
        "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
        "Accept":"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }
    req = request.Request(url, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read()
    # 解析html
    html =  etree.HTML(html)
    return html

words = []

def get_word(html):
    tr_list = html.xpath("//tr")
    # 遍历每个tr元素，每一个tr对应一个单词和介绍
    for tr in tr_list:
        '''
        查找相应的单词和介绍
        '''
        word = {}
        strong = tr.xpath('.//strong')
        if len(strong):
            # strip把找到的内容去掉空格
            name = strong[0].text.strip()
            word['name'] = name

        # 查找单词的释义
        td_content = tr.xpath('./td[@class="span10"]')
        if len(td_content):
            content = td_content[0].text.strip()
            word['content'] = content

        if word != {}:
            words.append(word)
    return words

def write_to_file(words):
   with open('words.txt', 'w', encoding='utf-8') as f:
       for word in range(len(words)):
           str = words[word]['name'] + ": " + words[word]['content']
           f.write(str + '\n')
           # f.write(json.dumps(str, ensure_ascii=False) + '\n')

if __name__ == '__main__':
    print('starting....')
    start_time = time.process_time()
    html = get_page(2)
    words = get_word(html)
    write_to_file(words)
    print('ending...')
    end_time = time.process_time()
    print('运行时间%s'%(end_time-start_time))
