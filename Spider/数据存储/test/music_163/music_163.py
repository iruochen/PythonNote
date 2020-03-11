'''
抓取网易云音乐

# 下载外链
http://music.163.com/song/media/outer/url?id=.mp3
http://music.163.com/song/media/outer/url?id=254574.mp3

引入tkinter / pyqt5

1. 获取页面源码：https://music.163.com/#/playlist?id=2465426779
2. 获取歌曲id以及歌曲名称
3. 下载音乐
'''

from tkinter import *
import requests
from urllib import request
from bs4 import BeautifulSoup
import os
import tkinter.messagebox

def music_spider():
    # 获取用户输入的url地址
    url = entry.get()
    if '#' in url:
        url = url.replace('#/', '')

    # url = 'https://music.163.com/playlist?id=2465426779'
    headers = {
        'referer': 'https://music.163.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }

    # 请求页面详情信息
    res = requests.get(url, headers=headers).text

    # < ul class ="f-hide" > < li > < a href="/song?id=254574" > 后来 < / a > < / li >

    # 创建soup对象
    soup = BeautifulSoup(res, 'lxml')
    # 获取歌曲id与歌曲名称

    music_dicts = {}
    items = soup.find('ul', {'class':'f-hide'}).find_all('a')
    for item in items:
        music_id = item.get('href').split('=')[-1]
        music_name = item.text
        music_dicts[music_id] = music_name

    for song_id in music_dicts:
        # 拼接歌曲下载url地址
        song_url = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(song_id)
        # print(song_url)

        # 设置下载路径
        root = 'music_163'
        if not os.path.exists(root):
            os.makedirs(root)

        # 添加数据到控件中
        text.insert(END, '正在下载: {}'.format(music_dicts[song_id]))
        # 文本框向下滚动
        text.see(END)
        # 更新
        text.update()

        # 现在不会重定向了, 所以下列代码用不到
        # res = requests.get(song_url, headers=headers)
        # print(res.status_code)
        # print(res.headers)
        # m_url = res.headers['Location']
        try:
            request.urlretrieve(song_url, root + '\\' + music_dicts[song_id] + '.mp3')
        except:
            print('{}下载失败'.format(music_dicts[song_id]))

def quit():
    quit = tkinter.messagebox.askokcancel('提示', '确定退出吗？')
    if quit == True:
        root.destroy()


# 创建窗口
root = Tk()

# 设置窗口标题
root.title('网易云音乐下载器')

# 设置窗口大小
root.geometry('850x550')

# 设置窗口位置
root.geometry('+550+200')
root.resizable(0, 0)

# 设置下载器标签：请输入您下载的地址
label = Label(root, text='请输入您的下载地址', font=('隶书', 22))
# 定位 pack place grid
label.grid()

# 设置输入框)
entry = Entry(root, font=('隶书',20), width=39)
entry.grid(row=0, column=1)

# 设置列表框
text = Listbox(root, font=('隶书',20), width=60, height=14)
text.grid(row=1, columnspan=2)

# 设置按钮 N S W E
button1 = Button(root, text='Start', font=('隶书', 25), command=music_spider)
button1.grid(row=2, column=0, sticky='s')  # sticky: 对齐方式

# 退出按钮
button2 = Button(root, text='Quit', font=('隶书', 25), command=quit)
button2.grid(row=2, column=1, sticky='s')

# 显示窗口, 显示x消息回环
root.mainloop()


if __name__ == '__main__':
    music_spider()
