from urllib import request, parse
from http import cookiejar

# 创建fileccookiejar的实例
filename = "cookie.txt"
cookie = cookiejar.MozillaCookieJar(filename)

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
        "email": "xxxx",
        "password": "xxxx"
    }

    # 把数据进行编码
    data = parse.urlencode(data)

    # 创建一个请求对象
    req = request.Request(url, data=data.encode())

    # 使用opener发起请求
    rsp = opener.open(req)

    # 保存cookie到文件

    # ignor_discard表示即使cookie将要被丢弃也要保存下来
    # ignor_expires表示如果该文件中cookie即使已经过期，保存
    cookie.save(ignore_discard=True, ignore_expires=True)


if __name__ == '__main__':
    login()
