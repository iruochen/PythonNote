'''
V2
处理js解密代码
'''

'''
通过查找，能找到js代码中操作代码

1. 这个是计算salt的公式  i = "" + (new Date).getTime() + parseInt(10 * Math.random(), 10);
2. sign: n.md5("fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj")
md5一共需要四个参数，第一个和第四个都是固定值的字符串，第三个参数是所谓的salt，
第二个参数就是输入的要查找的单词

'''

def getSalt():
    '''
    salt的公式是： "" + (new Date).getTime() + parseInt(10 * Math.random(), 10);
    把他翻译成python代码
    :return: salt
    '''
    import time, random

    salt = int(time.time()*1000) + random.randint(0, 10)

    return salt

def getMD5(v):
    '''

    :param v:
    :return: sign
    '''
    import hashlib
    md5 = hashlib.md5()

    # update需要一个bytes格式的参数
    md5.update(v.encode('utf-8'))
    sign = md5.hexdigest()

    return sign

def getSign(key, salt):

    sign = "fanyideskweb" + key + str(salt) + "n%A-rKaT5fb[Gy?;N5@Tj"
    sign = getMD5(sign)

    return sign

from urllib import request, parse

def youdao(key):

    # url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

    salt = getSalt()

    data = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": str(salt),
        "sign": getSign(key, salt),
        "ts": "1569052320722",
        "bv": "a4f4c82afd8bdba188e568d101be3f53",
        "doctype": "json",
        "version": "2.1"
    }

    # 参数data需要时bytes格式
    data = parse.urlencode(data).encode()

    headers = {
        "Accept": "application / json, text / javascript, * / *; q = 0.01",
        # "Accept - Encoding": "gzip, deflate",
        "Accept - Language": "zh - CN, zh;q = 0.9",
        "Connection": "keep - alive",
        "Content - Length": len(data),
        "Content - Type": "application / x - www - form - urlencoded;charset = UTF - 8",
        "Cookie": "OUTFOX_SEARCH_USER_ID = -1916336379 @ 10.169.0.84;JSESSIONID = aaaF3jqgNCov6fQWqZs1w;OUTFOX_SEARCH_USER_ID_NCOO = 885890211.5426716;___rl__test__cookies = 1569052795328",
        "Host": "fanyi.youdao.com",
        "Origin": "dhttp: // fanyi.youdao.com",
        "Referer": "http: // fanyi.youdao.com/",
        "User - Agent": "Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 76.0.3809.132Safari / 537.36",
        "X - Requested - With": "XMLHttpRequest"
    }

    req = request.Request(url=url, data=data, headers=headers)
    rsp = request.urlopen(req)

    html = rsp.read().decode()
    print(html)

if __name__ == '__main__':
    m = input()
    youdao(m)

