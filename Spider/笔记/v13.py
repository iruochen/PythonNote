from urllib import request, parse
from http import cookiejar

# 创建ccookiejar的实例
cookie = cookiejar.CookieJar()

# 生成cookie的管理器
cookie_handle = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handle = request.HTTPHandler()
# 生成https管理器
https_handle = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handle, https_handle, cookie_handle)

def login():
    '''
    负责初次登陆
    需要输入用户名密码，用来获取登陆cookie凭证
    :return:
    '''

    # 此url需要从登录form的action属性中提取
    url = "http://www.renren.com/PLogin.do"

    # 此键值需要从登陆form的两个对应input中提取name属性
    data = {
        "email": "xxx - xxxx - xxxx",
        "password": "xxxxxxx"
    }

    # 把数据进行编码
    data = parse.urlencode(data)

    # 创建一个请求对象
    req = request.Request(url, data=data.encode())

    # 使用opener发起请求
    rsp = opener.open(req)

def getHomePage():
    url = "http://www.renren.com/972301090/profile"

    # 如果已经执行了login函数，则opener自动已经包含相应的cookie值
    rsp = opener.open(url)

    html = rsp.read().decode()

    with open("rsp.html", "w", encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    login()
    getHomePage()
