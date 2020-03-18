'''
url = 'http://api.map.baidu.com/place/v2/detail?uid=435d7aea036e54355abbbcc8&output=json&scope=2&ak=您的密钥 '

'''
import requests
import json
from Spider.baiduMap_API.MySQLAPI import Sql

def get_json(uid):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/80.0.3987.132 Safari/537.36'
    }
    data = {
        'uid': uid,
        'scope': '2',
        'output': 'json',
        'ak': 'GCf1BxFkAnmtrCireC0XN5EQ4q5jHPaC'
    }

    url = 'http://api.map.baidu.com/place/v2/detail'
    res = requests.get(url, params=data, headers=headers)
    # decodejson = res.json()
    decodejson = json.loads(res.text)
    return decodejson

# 从数据库中获取uid号
results = Sql.read_city()
# print(type(results[0]))  # 类型为元组
for item in results:
    uid = item[0]
    decodejson = get_json(uid)
    # print(decodejson)
    infos = decodejson['result']

    # 获取想要的信息
    try:
        # uid
        uid = infos['uid']
    except:
        uid = None
    try:
        # street_id
        street_id = infos['street_id']
    except:
        street_id = None
    try:
        # park_name
        park_name = infos['name']
    except:
        park_name = None
    try:
        # address
        address = infos['address']
    except:
        address = None
    try:
        # shop_hours
        shop_hours = infos['detail_info']['shop_hours']
    except:
        shop_hours = None
    try:
        # detail_url
        detail_url = infos['detail_info']['detail_url']
    except:
        detail_url = None
    try:
        # content_tag
        content_tag = infos['detail_info']['content_tag']
    except:
        content_tag = None
    print(uid, street_id, park_name, address, shop_hours, detail_url, content_tag)
    Sql.insert_park(uid, street_id, park_name, address, shop_hours, detail_url, content_tag)
