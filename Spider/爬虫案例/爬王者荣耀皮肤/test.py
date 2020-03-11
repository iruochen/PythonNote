import os
import requests
import time

url = 'https://pvp.qq.com/web201605/js/herolist.json'
herolist = requests.get(url)  # 获取英雄列表json文件

herolist_json = herolist.json()  # 转化为json格式
hero_name = list(map(lambda x:x['cname'], herolist.json()))  # 提取英雄名字
hero_num = list(map(lambda x:x['ename'], herolist.json()))  # 提取英雄编号

# print(hero_name)
# print(hero_num)

# 下载图片
def downloadPic():
    print('运行中............')
    i = 0
    for j in hero_num:
        # 创建文件夹
        os.mkdir("D:\\wzry\\" + hero_name[i])
        # 进入创建好的文件夹
        os.chdir("D:\\wzry\\" + hero_name[i])
        i += 1
        for k in range(10):
            # 拼接url
            onehero_link = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(j) + '/' + str(
                j) + '-bigskin-' + str(k) + '.jpg'
            im = requests.get(onehero_link)  # 请求url
            if im.status_code == 200:
                open(str(k) + '.jpg', 'wb').write(im.content)  # 写入文件

if __name__ == '__main__':
    print('开始时间: {}'.format(time.ctime()))
    downloadPic()
    print('结束时间: {}'.format(time.ctime()))