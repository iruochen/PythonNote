import json
import time

import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains

# 重写联打码的API
def catch():
    '''
            main() 参数介绍
            api_username    （API账号）             --必须提供
            api_password    （API账号密码）         --必须提供
            file_name       （需要识别的图片路径）   --必须提供
            api_post_url    （API接口地址）         --必须提供
            yzm_min         （识别结果最小长度值）        --可空提供
            yzm_max         （识别结果最大长度值）        --可空提供
            yzm_type        （识别类型）          --可空提供
            tools_token     （V1软件Token）     --可空提供
    :return:
    '''
    api_username = ''
    api_password = ''
    file_name = 'c:/temp/lianzhong_vcode.png'
    api_post_url = "http://v1-http-api.jsdama.com/api.php?mod=php&act=upload"
    yzm_min = ''
    yzm_max = ''
    yzm_type = ''
    tools_token = ''

    # proxies = {'http': 'http://127.0.0.1:8888'}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
        # 'Content-Type': 'multipart/form-data; boundary=---------------------------227973204131376',
        'Connection': 'keep-alive',
        'Host': 'v1-http-api.jsdama.com',
        'Upgrade-Insecure-Requests': '1'
    }

    files = {
        'upload': (file_name, open(file_name, 'rb'), 'image/png')
    }

    data = {
        'user_name': api_username,
        'user_pw': api_password,
        'yzm_minlen': yzm_min,
        'yzm_maxlen': yzm_max,
        'yzmtype_mark': yzm_type,
        'zztool_token': tools_token
    }
    s = requests.session()
    # r = s.post(api_post_url, headers=headers, data=data, files=files, verify=False, proxies=proxies)
    r = s.post(api_post_url, headers=headers, data=data, files=files, verify=False)
    print(r.text)
    return r.text

class Login(object):
    def __init__(self):
        url = ""
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()

    def send(self):
        self.driver.implicitly_wait(6)
        username_input =