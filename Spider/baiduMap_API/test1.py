'''
注册百度地图API账号并进行开发者认证
目标：获取全国公园信息并保存至 MySQL 数据库中

地点检索详情链接
http://api.map.baidu.com/place/v2/detail?uid=435d7aea036e54355abbbcc8&output=json&scope=2&ak=您的密钥 //GET请求

基础地址
http://api.map.baidu.com/place/v2/search?
参数：
    query: 公园
    region: 太原市
    scope: 2
    page_size: 20
    output: json
    ak: GCf1BxFkAnmtrCireC0XN5EQ4q5jHPaC
'''

import requests

def get_json(loc, page_num=0):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/80.0.3987.132 Safari/537.36'
    }
    data = {
        'q': '公园',
        'region': loc,
        'scope': '2',
        'page_size': 20,
        'page_num': page_num,
        'output': 'json',
        'ak': 'GCf1BxFkAnmtrCireC0XN5EQ4q5jHPaC'
    }

    url = 'http://api.map.baidu.com/place/v2/search'
    res = requests.get(url, params=data, headers=headers)
    print(res.url)
    decodejson = res.json()

    return decodejson

a = get_json('太原市')
print(a)
