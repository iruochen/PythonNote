import requests
from bs4 import BeautifulSoup
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

def pparser():

    # 发起请求
    basic_url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html'

    headers = {'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    response = requests.get(
                basic_url,
                headers=headers,
                timeout=10)

    # 设置网页编码
    response.encoding = 'utf-8'

    # 返回文本数据
    htm = response.text

    # 解析内容
    soup = BeautifulSoup(htm, 'lxml')
    # 获取页数信息
    page = int(soup.find('p', attrs={"class": "pg"}).find_all('strong')[0].text)

    # url前缀
    url_part = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list'

    # 分页获取每一页的开奖信息
    for i in range(1, page+1):
        url = url_part + '_' + str(i) + '.html'

        res = requests.get(url, headers=headers, timeout=10)
        res.encoding = 'utf-8'
        context = res.text
        soups = BeautifulSoup(context, 'lxml')

        # 数据提取单元
        if soups.table is None:
            continue
        elif soups.table:
            table_rows = soups.table.find_all('tr')
            # 第二行到倒数第一行为双色球数据
            for row_num in range(2, len(table_rows)-1):
                row_tds = table_rows[row_num].find_all('td')
                # 双色球号码
                ems = row_tds[2].find_all('em')
                # 开奖日期，期号，红色球1号-6号，蓝色球
                result = row_tds[0].string + ',' + row_tds[1].string + ',' + ems[0].string + ' ' + ems[1].string + ' ' + \
                    ems[2].string + ' ' + ems[3].string + ' ' + ems[4].string + ' ' + ems[5].string + ', ' + ems[6].string
                print(result)

                # 保存至文件
                save_to_file(result)

                red_num.append(ems[0].string) # 红色球1
                red_num.append(ems[1].string) # 红色球2
                red_num.append(ems[2].string) # 红色球3
                red_num.append(ems[3].string) # 红色球4
                red_num.append(ems[4].string) # 红色球5
                red_num.append(ems[5].string) # 红色球6
                blue_num.append(ems[6].string) # 蓝色球
            else:
                continue

    return red_num, blue_num

def save_to_file(content):
    with open('ssq.text', 'a', encoding='utf-8') as f:
        f.write(content + '\n')

def predict(red_num, blue_num):
    '''
    :param red_num: 红色球列表
    :param blue_num: 蓝色球列表
    :return:
    '''

    # Counter：遍历列表所有元素，记录元素出现的次数
    red_count = Counter(red_num)
    blue_count = Counter(blue_num)

    print('---------------------------------------------------')
    # 按照出现频率倒序
    # items()将red_count、blue_count转化为可迭代对象
    # key = lambda x:x[1] 为对前面对象中的第二维数据（即value）的值进行排序  key = lambda 变量: 变量[维数]
    red_sorted = sorted(red_count.items(), key=lambda x: x[1], reverse=False)
    blue_sorted = sorted(blue_count.items(), key=lambda x: x[1], reverse=False)
    # 记录前6个高频红色球
    red = red_sorted[0:6]

    # 记录前3个高频蓝色球
    blue = blue_sorted[0:3]

    # 第一维度
    red = list(map(lambda x:x[0], red))
    blue = list(map(lambda x:x[0], blue))

    # 排序
    red.sort()
    blue.sort()

    print('号码低频-1注: '+str(red)+' | '+blue[0])
    print('号码低频-2注: '+str(red)+' | '+blue[1])
    print('号码低频-3注: '+str(red)+' | '+blue[2])

    print('---------------------------------------------------')
    # 按照出现频率顺序
    red_sorted = sorted(red_count.items(), key=lambda x: x[1], reverse=True)
    blue_sorted = sorted(blue_count.items(), key=lambda x: x[1], reverse=True)

    blue_sorted_count = list(map(lambda x:x[1], blue_sorted))
    blue_ball = list(map(lambda x:x[0], blue_sorted))
    plt.rcParams['font.family'] = ['STFangsong']
    plt.bar(blue_ball, blue_sorted_count, align='center')
    plt.title('蓝色球直方图')
    plt.ylabel('出现次数')
    plt.xlabel('球号')
    plt.show()

    red = red_sorted[0:6]
    blue = blue_sorted[0:3]

    red = list(map(lambda x:x[0], red))
    blue = list(map(lambda x:x[0], blue))
    red.sort()
    blue.sort()
    print('号码高频-1注: '+str(red)+' | '+blue[0])
    print('号码高频-2注: '+str(red)+' | '+blue[1])
    print('号码高频-3注: '+str(red)+' | '+blue[2])

if __name__ == '__main__':
    # 定义两个变量，用于记录历史开奖信息中的红球、蓝球号码信息
    red_num = []
    blue_num = []
    # 调用函数，用于获取并解析开奖的数据
    pparser()
    # 分析数据并预测未来的开奖信息
    predict(red_num, blue_num)