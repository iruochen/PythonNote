import requests
import json

def get_json(loc, page_num=0):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/80.0.3987.132 Safari/537.36'
    }
    data = {
        'query': '公园',
        'region': loc,
        'scope': '2',
        'page_size': 20,
        'page_num': page_num,
        'output': 'json',
        'ak': 'GCf1BxFkAnmtrCireC0XN5EQ4q5jHPaC'
    }

    url = 'http://api.map.baidu.com/place/v2/search'
    res = requests.get(url, params=data, headers=headers)
    # decodejson = res.json()
    decodejson = json.loads(res.text)
    return decodejson

province_list = ['四川省', '山东省', '甘肃省', '浙江省', '陕西省', '山西省', '河北省', '江苏省', '河南省']
for province in province_list:
    decodejson = get_json(province)
    for eachcity in decodejson['results']:
        # print(eachcity)
        city = eachcity['name']
        num = eachcity['num']
        output = '\t'.join([city, str(num)]) + '\n'
        with open('cities.txt', 'a', encoding='utf-8') as f:
            f.write(output)
