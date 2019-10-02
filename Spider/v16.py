from urllib import request, parse
from http import cookiejar

# 创建ccookiejar的实例
cookie = cookiejar.MozillaCookieJar()
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)

# 生成cookie的管理器
cookie_handle = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handle = request.HTTPHandler()
# 生成https管理器
https_handle = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handle, https_handle, cookie_handle)

def getHomePage():
    url = "http://www.renren.com/972301090/profile"

    # 如果已经执行了login函数，则opener自动已经包含相应的cookie值
    rsp = opener.open(url)

    html = rsp.read().decode()

    with open("rsp.html", "w", encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    getHomePage()
