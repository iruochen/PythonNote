import requests

url = 'https://item.jd.com/1250438.html'
try:
    # 发起get请求
    response = requests.get(url)
    # 获取状态码
    # 爬取页面可使用状态码判断
    print(response.status_code)
    # 获取完整url地址
    print(response.url)
    # 获取原文编码类型
    print(response.apparent_encoding)
    # 解决页面乱码
    response.encoding = response.apparent_encoding
    # 响应得到字符串
    print(type(response.text))
    # 响应得到bytes
    print(type(response.content))
    # print(response.text)
    # 返回cookie对象
    CookieJar = response.cookies
    # 将cookie转为字典
    cookiedict = requests.utils.dict_from_cookiejar(CookieJar)
    print(cookiedict)
except:
    print('爬取失败')