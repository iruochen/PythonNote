'''
urllib 登陆华为官网
url = 'https://www.huawei.com/en/accounts/LoginPost'
method: post
pram:
    userName: 1910888666@qq.com
    pwd: D0c+4RZ4VvrMm8XD+Yz12V1seSZ3MeeD7Xc84Imz6jCSd1nw3U9h8ATPnUXUv6rQ9Le09eJmluiXNFlrmfbhsfHBDKiSWkrRICwLxiPApOrJ8cD08UQ+p40hNWbK1368llH2zNg6Pnzny9MD2B7drZ+ty3e4jLGuaLxWsAMmi7o=
    languages: zh
    fromsite: www.huawei.com
    authMethod: password
'''

from urllib import request, parse
from http import cookiejar

# 生成cookie对象
cookie = cookiejar.CookieJar()
# 生成cookie管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 生成http请求管理器
http_handler = request.HTTPHandler()
# 生成https请求管理器
https_handler = request.HTTPSHandler()

# 构建发起请求管理器
opener = request.build_opener(cookie_handler, http_handler, https_handler)


# 构建登陆函数
def login(url):
    data = {
        'userName': '1441865605@qq.com',
        'pwd': 'ruochen666',
        'languages': 'zh',
        'fromsite': '',
        'authMethod': 'password'
    }
    data = parse.urlencode(data)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
    }
    # data 数据类型为bytes
    req = request.Request(url, data=bytes(data, encoding='utf-8'), headers=headers)
    content = opener.open(req)
    content = content.read().decode()
    print(content)

if __name__ == '__main__':
    url = 'https://www.huawei.com/en/accounts/LoginPost'
    login(url)