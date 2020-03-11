import io
from PIL import Image
import numpy as np
import requests

def get_word(ch, quality):
    '''
    获取单个汉字（字符）的图片
    :param ch: 单个汉字或英文字母（仅支持大写）
    :param quality: 单字分辨率，H-640像素，M-480像素，L-320像素
    :return: 图片尺寸元组
    '''

    # BytesIO: 在内存中读写bytes
    fp = io.BytesIO(requests.post(url='', data={'ch':ch}).content)
    im = Image.open(fp)
    w, h = im.size
    if quality == 'M':
        w, h = int(w*0.75), int(h*0.75)
    elif quality == 'L':
        w, h = int(w*0.5), int(h*0.5)

    return im.resize((w, h))

def get_bg(quality):
    '''
    获取春联背景图片
    :param quality:
    :return:
    '''

    return get_word('bg', quality)

def write_couplets(text, Horv='V', quality='L', out_file=None):
    '''
    生成春联
    :param text: 春联内容，以空格断行
    :param Horv: H-横排，V-竖排
    :param quality: 单字分辨率，H-640像素，M-480像素，L-320像素
    :param out_file: 输出文件名
    :return:
    '''

    usize = {'H':(640,23), 'M':(480, 18), 'L':(320, 12)}
    bg_im = get_bg(quality)
    # text.split() 分割字符
    text_list = [list(item) for item in text.split()]
    rows = len(text_list)
    cols = max([len(item) for item in text_list])

    if Horv == 'V':
        # 竖排
        ow, oh = 40+rows*usize[quality][0]+(rows-1)*10, 40+cols*usize[quality][0]
    else:
        # 横排
        ow, oh = 40+cols*usize[quality][0], 40+rows*usize[quality][0]+(rows-1)*10

    out_im = Image.new('RGBA', (ow, oh), '#f0f0f0')

    for row in range(rows):
        if Horv == 'V':
            row_im = Image.new('RGBA', (usize[quality][0], cols*usize[quality][0], 'white'))
            offset = (ow-(usize[quality][0]+10)*(row+1)-10, 20)
        else:
            row_im = Image.new('RGBA', (cols * usize[quality][0], usize[quality][0]), 'white')
            offset = (20, 20 + (usize[quality][0] + 10) * row)

        for col, ch in enumerate(text_list[row]):
            if Horv == 'V':
                pos = (0, col*usize[quality][0])
            else:
                pos = (col*usize[quality][0], 0)

            ch_im = get_word(ch, quality)
            row_im.paste(bg_im, pos)
            row_im.paste(ch_im, (pos[0]+usize[quality][1], pos[1]+usize[quality][1]), mask=ch_im)

        out_im.paste(row_im, offset)

    if out_file:
       out_im.convert('RGB').save(out_file)
    out_im.show()

text = ""
write_couplets(text, 'v', 'M', out_file='')





